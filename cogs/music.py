import discord
from discord import app_commands
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        try:
            voice_channel = ctx.author.voice.channel
            if ctx.voice_client is None:
                await voice_channel.connect()

            ydl_opts = {
                'format': 'bestaudio/best',
                'noplaylist': True,
                'quiet': True
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['url']
                title = info.get('title', 'Desconhecido')

            ctx.voice_client.stop()
            ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=url2), after=lambda e: print('Feito!', e))

            await ctx.send(f"RICKROLL!!!1!!11")
        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")
        

    @commands.command()
    async def pause():
        pass

    @commands.command()
    async def stop():
        pass
    
async def setup(bot):
    await bot.add_cog(Music(bot))