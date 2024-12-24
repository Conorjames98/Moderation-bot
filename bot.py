import discord
# audioop-lts (Long-Term-Support) is a backport of the audioop module from Python 3.9. It provides the same API as the original module, but works with Python 3.6, 3.7, and 3.8.
# this fixes the error "ModuleNotFoundError: No module named 'audioop'"
import audioop
import os

from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True
#Creating an instance of a client this client is our connection to discord
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Hello'):
        await message.channel.send('Hello!')

client.run(DISCORD_TOKEN)
