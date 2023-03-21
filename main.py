


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from chatgpt import message_response

load_dotenv()


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is ready")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!gpt") and len(message.content) >= 4:

        await message.channel.send(message_response(message.content[4:]))

client.run(os.getenv("DISCORD_TOKEN"))


"!gpt hello world"