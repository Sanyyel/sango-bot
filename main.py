import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import yt_dlp

load_dotenv(".env")
TOKEN: str = os.getenv("token_bot")
FFMPeg = os.getenv("path_ffmpeg")

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
permissoes.voice_states = True
bot = commands.Bot(command_prefix="!", intents=permissoes)

async def load_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}")

@bot.event
async def on_ready():
    await load_cogs()
    print("I'm ready!")

@bot.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Olá, {usuario}!")

@bot.command()
async def apresentacao(ctx:commands.Context):
    usuario = ctx.author
    await ctx.send(f"Olá, {usuario}. Eu sou uma DiscordBot em criação. Fique atento(a) para novas funcionalidades em breve!")

"""@bot.event #rickroll meme
async def on_message(message):
    if message.author.bot:
        return
    
    mensagem = str(message.content)
    if mensagem.index("?") > -1:
        await message.channel.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    """

"""@bot.command()
async def rickroll(ctx:commands.Context):
    await ctx.reply("https://www.youtube.com/watch?v=dQw4w9WgXcQ")"""

bot.run(TOKEN)