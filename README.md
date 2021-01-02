```                               _____
                                 |     |
                                 | | | |
                                 |_____|
                           ____ ___|_|___ ____
                          ()___)         ()___)
                          // /|           |\ \\
                         // / |           | \ \\
                        (___) |___________| (___)
                        (___)   (_______)   (___)
                        (___)     (___)     (___)
                        (___)      |_|      (___)
                        (___)  ___/___\___   | |
                         | |  |           |  | |
                         | |  |___________| /___\
                        /___\  |||     ||| //   \\
                       //   \\ |||     ||| \\   //
                       \\   // |||     |||  \\ //
                        \\ // ()__)   (__()
                              ///       \\\
                             ///         \\\
                           _///___     ___\\\_
                          |_______|   |_______|```
# py-bot

### Usage
Docker is chosen method to deploy this bot, but you may simply run install the depnedencies specified here an run the main python file

**Commands for those unfamiliar with docker but would like to try it out**

*while in cloned repo*
- `docker build -t <chosen tag> .`
- `docker run -it --name <chosen name> <chosen tag>` *-it flag is there mainly for stdout and stderr but it will also allow you to easily stop the container with a kill command* See: [docker run reference](https://docs.docker.com/engine/reference/run/)
- `docker ps` list currently running containers
- `docker stop <container name>` stop container by name listed in `docker ps` output

### Dependencies
RUN `python3 -m pip install -U <package name>` *-U flag is not required and will update all packages*
Include packge name as shown bellow
- `discord.py[voice]` *installing this seems to install it's dependecies despite the documentation saying otherwise* See: [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)