## Henk's Mod for Alpaca models

These are the modifications I used in my ALsy Discord bot showcase, the characters support has been crippled to only use the char\_name and char\_persona.  
Instead of the pygmalion / character card format it expects the char\_persona to be written as an Alpaca instruction.

The personality of ALsy has been bundled so people can reproduce the bot. models I ran in the past were GPT4-X-Alpaca, Airoboros and Chronos.

## \----

## Project Description

This project is actively being developed and aims to evolve into a chatbot with a specified personality that can also serve as a personal assistant. The most recent changes have been made in the branch called "langchain." The intention is to migrate the main branch to use langchain once all the bugs have been resolved.

## Current Development Goals

*   Implement web browsing capabilities.
*   Enable document summarization, website interaction, and chat with documents and websites.
*   Enhance the chatbot's ability to follow instructions similar to chatGPT, especially with instruct models like alpaca.
*   Integrate infinite memory using chromadb.
*   Improve image detection by leveraging the LLM and blip2 instruct models, similar to llava.
*   Provide the bot with access to readily available langchain tools, (think chatGPT4 plugins)
*   AGI?!?!?

## Original Info Card: Discord Tavern Style LLM Chatbot

This Discord bot utilizes LLMs and character cards for casual chatting. The bot supports JSON files and tavern cards, offering the option to automatically update the bot's image and name.

![image](https://i.imgur.com/VPzquLom.png)

## Instructions

1.  Clone the repository.
2.  Modify the variables in the sample.env file and save it as .env in the same folder.
3.  Run the setup.bat file.
4.  Run the run.bat file.
5.  Choose the character.

![Choose](https://i.imgur.com/qY6ZpB8.png)

Please note that Discord only allows bots to be renamed twice per hour.

## More Information

*   DISCORD\_BOT\_TOKEN: Obtain this token from the Discord Developer Portal. [Guide for setting that up](https://rentry.org/discordbotguide)
*   ENDPOINT: Set the endpoint variable with the KoboldAI URL obtained from this [colab](https://colab.research.google.com/github/koboldai/KoboldAI-Client/blob/main/colab/GPU.ipynb). Simply press Shift + Enter to run the cells until you acquire the API URL. Alternatively, if you have a powerful GPU, you can run Kobold locally using [Kobold](https://github.com/KoboldAI/KoboldAI-Client) or its [Kobold 4bit fork](https://github.com/0cc4m/KoboldAI).  
    For more information on running it locally, refer to: [Local Installation (GPU)](https://docs.alpindale.dev/local-installation-(gpu)/kobold/)

## Slash Commands

Currently, these commands are primarily useful for developers. If you don't see them, use the `/sync` command to force their appearance.

| Command Name | Slash Command | More Info |
| --- | --- | --- |
| Sync Commands | `/sync` | Forces the slash commands to appear immediately. |
| Reload Cog | `/reload <name>` | Reloads a specific cog instead of restarting everything. |
| Regenerate Last Message | `/regenerate` | Removes the last message and generates another one. |

## Tip for making the .env file

## Enable file name extensions

\> Windows 11:

![win11img](https://i.imgur.com/HayEcPol.png)  
\> Windows 10:

![win10img](https://i.imgur.com/BsmMUjo.png)

## Now you can easily rename it to .env

![envgif](https://github.com/ausboss/PygDiscordBot/blob/main/how-to-env.gif)