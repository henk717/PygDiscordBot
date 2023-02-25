# Paperspace Branch
This branch Aims for easy use on paperspace. I used a pytorch environment with a GPU that has 24gb VRAM. I will test other gpus.

# Blip Image detection added
![image](https://i.imgur.com/VPzquLol.png)

# Discord Tavern Style Pygmalion Chatbot
This is a discord bot that uses Pygmalion-6B and a KoboldAI url. The bot now supports json files and tavern cards and will change its name and image automatically. I plan on adding more features like group chat support, random messages, and the ability to comment on images you share.

![Preview](https://i.imgur.com/XcIDQ3V.png)


# Instructions: 
>1. Clone the repo.

>2. Change the environment variables 

you pull up the shell and run this
```shell
nano ~/.bashrc
```
you add this to the environment variables
with nano text editor
```
export DISCORD_BOT_TOKEN=""
export PERIOD_IGNORE="False"
export CHANNEL_ID=1078702396942095
```
ctrl+x and save

then run this command
```shell
source ~/.bashrc
pip install -r requirements.txt
pip install --upgrade transformers
```

>3. Choose the character

![Choose](https://i.imgur.com/qY6ZpB8.png)

Discord only allows bots to be renamed twice per hour.

[Get more Characters](https://booru.plus/+pygmalion)
# More Info: 

DISORD_BOT_TOKEN: You can get this from the discord developers portal. [Guide for setting that up](https://rentry.org/discordbotguide)


