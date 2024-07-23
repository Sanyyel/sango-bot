import discord
from discord.ext import commands
from discord import app_commands

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

@bot.event
async def on_message(ctx:commands.Context):
    pass
    


bot.run("")