import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="emma", intents=intents)
@bot.event
async def on_ready():
    print(f"{bot.user} se ha activado corrrectamente.")

@bot.command()
async def prueba(ctx):

    canal = bot.get_channel(1527102240412799067)

    embed = discord.Embed(
        description=("aprobando, prueba pasada"),
        color=0xbf58ca
    )
    await canal.send(embed=embed)

    
import os
from dotenv import load_dotenv

load_dotenv()

bot.run(os.getenv("TOKEN"))
