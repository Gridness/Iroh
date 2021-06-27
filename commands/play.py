import discord
from discord import utils
from discord import guild
from discord.ext import commands
from discord_slash import SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option, SlashCommandOptionType
import youtube_dl
import random

from utils.build_embed import build_embed
from utils.phrases import *


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.is_playing = False
        self.song_queue = {}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
        'options': '-vn'}
        self.YTDL_OPTIONS = {'format': 'bestaudio', 'skip_download': True}

    def setup(client):
        client.add_cog(Music(client))

    @cog_ext.cog_slash(
        name="play",
        description="Начнем музыкальную ночь!",
        options=[
            create_option(
                name="url",
                description="Хочешь что-то конкретное?",
                option_type=SlashCommandOptionType.STRING,
                required=False
            )
        ]
    )
    async def play(self, ctx: SlashContext, url):
        if ctx.author.voice is None:
            await ctx.send(build_embed(self.client, random.choice(errorPhrases), "Нельзя слушать музыку с закрытыми ушами!", discord.Color.red, False, False))
    
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        vc = ctx.voice_client
        if url is not None:
            with youtube_dl.YoutubeDL(self.YTDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **self.FFMPEG_OPTIONS)
                vc.play(source)
                await ctx.send(build_embed(self.client, random.choice(playPhrases), info.get('title', None), discord.Color.orange, False, True, str(self.client.user)))
        else:
            with youtube_dl.YoutubeDL(self.YTDL_OPTIONS) as ydl:
                search_info = ydl.extract_info("ytsearch:eraser f64")

                for i in search_info:
                    print(i)