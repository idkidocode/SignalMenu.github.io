import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f"logged in as {self.user}!")


intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)

client.run('MTQ5MDM2NTcyNjc0NDM3OTUzNA.G162xT.Iqv0NOO1h9UgOIxcKPSBcWf2R7UdXwbg1I1tTw')
