import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option, SlashCommandOptionType
from discord_components import DiscordComponents, Button, ButtonStyle
import youtube_dl
import random

from utils.build_embed import build_embed
from utils.music_handling.search_yt import search_yt
from utils.command_log import command_log
from utils.phrases import *

from utils.singletons.song_queue_singleton import SongQueue
from utils.music_handling.play_music import play_music

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.slash = SlashCommand(self.client, sync_commands=True)
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 
        'options': '-vn'}
        self.YTDL_OPTIONS = {'format': 'bestaudio', 'skip_download': True}
        self.vc = ""

    def setup(client):
        client.add_cog(Music(client))

    # def play_next(self):
    #     if len(self.song_queue) > 0:
    #         self.is_playing = True
# 
    #         extracted_url = self.song_queue[0][0]['source']
# 
    #         self.song_queue.pop(0)
# 
    #         self.vc.play(discord.FFmpegAudio(extracted_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    # async def play_music(self):
    #     if len(self.song_queue) > 0:
    #         self.is_playing = True
    #         
    #         extracted_url = self.song_queue[0][0]['source'] 
# 
    #         if self.vc == "" or not not self.vc.is_connected():
    #             self.vc = await self.song_queue[0][1].connect()
    #         else:
    #             self.vc = await self.client.move_to(self.song_queue[0][1])
# 
    #         print(self.song_queue)
    #         self.song_queue.pop(0)
# 
    #         self.vc.play(discord.FFmpegAudio(extracted_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    @cog_ext.cog_slash(
        name="play",
        description="Начнем музыкальную ночь!"
        # options=[
        #     create_option(
        #         name="url",
        #         description="Хочешь что-то конкретное?",
        #         option_type=SlashCommandOptionType.STRING,
        #         required=False
        #     )
        # ]
    )
    async def play(self, ctx: SlashContext, *args):
        command_log("play", ctx)

        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send(build_embed())
        else:
            song = search_yt(self.YTDL_OPTIONS, query)
            if type(song) == type(True):
                await ctx.send(build_embed())
            else:
                await ctx.send(build_embed())
                SongQueue().song_queue.append([song, voice_channel])

                if self.is_playing is False:
                    await play_music(self.client, self.vc, SongQueue().song_queue, self.FFMPEG_OPTIONS)
