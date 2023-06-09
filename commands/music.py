import discord
from discord.ext import commands
import yt_dlp as youtube_dl


class Music(commands.Cog):
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 \
            -reconnect_streamed 1 \
            -reconnect_delay_max 5',
        'options': '-vn'}

    YDL_OPTIONS = {'format': 'bestaudio/best'}

    def __init__(self, client):
        self.client = client

    @commands.command(name="join", help="Chama o bot para a sala")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Você não está em um canal de voz!")

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command(name="stop", help="Expulsa o bot da sala")
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(name="play", help="Inicia música no bot. Argumentos: URL da música")
    async def play(self, ctx, url):
        await self.join(ctx)

        ctx.voice_client.stop()

        vc = ctx.voice_client

        try:
            with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPEG_OPTIONS)
                vc.play(source)
        except Exception as error:
            print(error)

    @commands.command(name="pause", help="Pausa a música atual")
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Pausado")

    @commands.command(name="resume", help="Continua a tocar a música pausada")
    async def resume(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Resume")


async def setup(bot):
    await bot.add_cog(Music(bot))
