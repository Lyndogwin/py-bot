import discord 

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(messaage))

client = MyClient()
client.run('Nzk0MzI5OTIxODEwOTg5MDg2.X-5PYw.ADWXwgU7G-3n1EhuX0zc-EudUG8')