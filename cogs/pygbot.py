"""
pygmalion cog
Peepy version

"""
import re
import json
import requests
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


# load the pre-trained model and tokenizer
revision = "dev"
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model = AutoModelForCausalLM.from_pretrained(
    "PygmalionAI/pygmalion-6b", revision=revision, torch_dtype=torch.float16
).to(device)
tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-6b")


# define the chatbot class
class Chatbot:
    def __init__(self, char_filename):
        # read character data from JSON file
        with open(char_filename, "r") as f:
            data = json.load(f)
            self.char_name = data["char_name"]
            self.char_persona = data["char_persona"]
            self.char_greeting = data["char_greeting"]
            self.world_scenario = data["world_scenario"]
            self.example_dialogue = data["example_dialogue"]

        # initialize conversation history and character information
        self.conversation_history = f"<START>\n{self.char_name}: {self.char_greeting}\n"
        self.character_info = f"{self.char_name}'s Persona: {self.char_persona}\nScenario: {self.world_scenario}\n"
        self.num_lines_to_keep = 20

    def prompt_tokens(self, prompt):
        # tokenize the prompt and return the number of tokens
        tokens = word_tokenize(prompt["prompt"])
        num_tokens = len(tokens)
        return num_tokens


    def generate_response(self, input_ids):
        # create attention mask tensor
        attention_mask = torch.ones_like(input_ids)

        output = model.generate(
        input_ids,
        max_length=2048,
        do_sample=True,
        use_cache=True,
        min_new_tokens=10,
        temperature=1.0,
        repetition_penalty=1.02,
        top_p=0.9,
        attention_mask=attention_mask,
        pad_token_id=tokenizer.pad_token_id,
        )
        if output is not None:
            generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
            return generated_text
        else:
            return "This is an empty message. Something went wrong. Please check your code!"

    def parse_text(self, generated_text):
        text_lines = [line.strip() for line in str(generated_text).split("\n")]
        aurora_line = next((line for line in reversed(text_lines) if 'AuroraAI' in line), None)
        if aurora_line is not None:
            aurora_line = aurora_line.replace('AuroraAI:', '').strip()
            for i in range(len(text_lines)):
                text_lines[i] = text_lines[i].replace('AuroraAI:', '')
        return aurora_line

    def save_conversation(self, message, message_content, bot):
        # add user response to conversation history
        self.conversation_history += f'{message.author.name}: {message_content}\n'
        print(f'self.conversation_history: {self.conversation_history}')

        # format prompt
        prompt = {
            "prompt": self.character_info + '\n'.join(
                self.conversation_history.split('\n')[-self.num_lines_to_keep:]) + f'{self.char_name}:',
        }

        input_ids = tokenizer.encode(prompt["prompt"], return_tensors="pt").to(device)
        results = self.generate_response(input_ids)

        text_lines  = [line.strip() for line in str(results).split("\n")]
        print(text_lines)
        bot_line = next((line for line in reversed(text_lines) if self.char_name in line), None)
        if bot_line is not None:
            bot_line = bot_line.replace(f'{self.char_name}:', '').strip()
            for i in range(len(text_lines)):
                text_lines[i] = text_lines[i].replace(f'{self.char_name}:', '')

        response_text = bot_line
        # response_text = ''.join(new_list)
        # add bot response to conversation history

        self.conversation_history += f'{self.char_name}: {response_text}\n'
        return response_text

    async def batch_save_conversation(self, message):
        # add user message to conversation history
        self.conversation_history += f"{message}\n"
        print(f'self.conversation_history: {self.conversation_history}')

        # format prompt
        prompt = {
            "prompt": self.character_info + '\n'.join(
                self.conversation_history.split('\n')[-self.num_lines_to_keep:]) + f'{self.char_name}:',
        }

        input_ids = tokenizer.encode(prompt["prompt"], return_tensors="pt").to(device)
        results = self.generate_response(input_ids)

        text_lines  = [line.strip() for line in str(results).split("\n")]
        print(text_lines)
        bot_line = next((line for line in reversed(text_lines) if self.char_name in line), None)
        if bot_line is not None:
            bot_line = bot_line.replace(f'{self.char_name}:', '').strip()
            for i in range(len(text_lines)):
                text_lines[i] = text_lines[i].replace(f'{self.char_name}:', '')

        response_text = bot_line
        # response_text = ''.join(new_list)
        # add bot response to conversation history

        self.conversation_history += f'{self.char_name}: {response_text}\n'
        return response_text



class ChatbotCog(commands.Cog, name="chatbot"):
    def __init__(self, bot):
        self.bot = bot
        self.chatbot = Chatbot("chardata.json")

    @commands.command(name="chat")
    async def chat_command(self, message: discord.Message, message_content, bot) -> None:
        # get response message from chatbot and return it
        response_message = self.chatbot.save_conversation(message, message_content, bot)
        return response_message

    @commands.command(name="batch_chat")
    async def batch_chat_command(self, channel, message_content) -> None:
        # get response message from chatbot and return it
        response = await self.chatbot.batch_save_conversation(message_content)
        return response


async def setup(bot):
    # add chatbot cog to bot
    await bot.add_cog(ChatbotCog(bot))
