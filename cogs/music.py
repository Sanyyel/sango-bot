import discord
from discord import app_commands
from discord.ext import commands
import yt_dlp

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()


    # PLAY COMMAND
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

            ffmpeg_options = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn',
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['url']
                title = info.get('title', 'Desconhecido')
                await ctx.send(f"URL obtido: {title}")

            ctx.voice_client.stop()
            ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=url2, **ffmpeg_options), after=lambda e: print('Feito!', e))

            await ctx.send(f"Áudio tocando...")
        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")
    
    # PAUSE COMMAND
    @commands.command()
    async def pause(self, ctx):
        try:
            if ctx.voice_client and ctx.voice_client.is_playing():
                ctx.voice_client.pause()
                await ctx.send("Áudio pausado.")
            else:
                await ctx.send("Não estou tocando nada agora.")
            

        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")
    
    # RESUME COMMAND
    @commands.command()
    async def resume(self, ctx):
        try:
            if ctx.voice_client and ctx.voice_client.is_paused():
                ctx.voice_client.resume()
                await ctx.send("Áudio despausado.")
            else:
                await ctx.send("Não estou tocando nada agora.")

        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")

    # STOP COMMAND
    @commands.command()
    async def stop(self, ctx):
        try:
            if ctx.voice_client and ctx.voice_client.is_playing():
                ctx.voice_client.stop()
                await ctx.send("Áudio pausado.")
            else:
                await ctx.send("Não estou tocando nada agora.")

        except Exception as e:
            await ctx.send(f"Ocorreu um erro: {str(e)}")
        
    
async def setup(bot):
    await bot.add_cog(Music(bot))