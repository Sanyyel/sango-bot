import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN: str = os.getenv("token_bot")

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
bot = commands.Bot(command_prefix="!", intents=permissoes)

@bot.event
async def on_ready():
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

@bot.command()
async def rickroll(ctx:commands.Context):
    await ctx.reply("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

bot.run(TOKEN)