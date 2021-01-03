```

██████╗░██╗░░░██╗░░░░░░██████╗░░█████╗░████████╗
██╔══██╗╚██╗░██╔╝░░░░░░██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝░╚████╔╝░█████╗██████╦╝██║░░██║░░░██║░░░
██╔═══╝░░░╚██╔╝░░╚════╝██╔══██╗██║░░██║░░░██║░░░
██║░░░░░░░░██║░░░░░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═╝░░░░░░░░╚═╝░░░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
```

### Usage
Docker is chosen method to deploy this bot, but you may simply run install the depnedencies specified here an run the main python file

**Commands for those unfamiliar with docker but would like to try it out**

*while in cloned repo*
- `docker build -t <chosen tag> .`
- `docker run -it --name <chosen name> <chosen tag>` *-it flag is there mainly for stdout and stderr but it will also allow you to easily stop the container with a kill command* See: [docker run reference](https://docs.docker.com/engine/reference/run/)
- `docker ps` list currently running containers
- `docker stop <container name>` stop container by name listed in `docker ps` output

### Required environment variables
Create a `bot.env` file in the top directory and add your bot token as `BOT_TOKEN='your-bot-hex-string'`. If you cloned this repo, the file will be git-ignored; otherwise, make sure this token is not publicly accessible.
See: [Environment varibales in Compose](https://docs.docker.com/compose/environment-variables/)

### Dependencies
RUN `python3 -m pip install -U <package name>` *-U flag is not required and will update all packages*
Include packge name as shown bellow
- `discord.py[voice]` *installing this seems to install it's dependecies despite the documentation saying otherwise* See: [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)

### Discord bot instrucitons
- Navigate to the [developers portal](https://discord.com/developers/applications)
- Create a new application and navigate to the bot tab
- Add a new bot
- Navigate to the OAuth2 tab
- Check bot
- Select permissions
- Navigate to the generated url in your browser
- Select the servers you wish to add the bot to 

## Goals
I would like to create a chat bot with the additional functionality of assisting in managing personal relationships by 'memorizing' important information about the people I converse with.

### NLP and other ML resources
- [Mimic Bot](https://adeshpande3.github.io/How-I-Used-Deep-Learning-to-Train-a-Chatbot-to-Talk-Like-Me)
- [Machine Learning Text](https://www.deeplearningbook.org/)