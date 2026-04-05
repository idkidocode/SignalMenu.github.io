import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"logged in as {self.user}!")


intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)

with open('example.txt', 'r') as f:
    content = f.read()


client.run(content)
