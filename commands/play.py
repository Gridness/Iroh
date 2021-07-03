import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_choice, create_option, SlashCommandOptionType
from discord_components import DiscordComponents, Button, ButtonStyle
import random
import datetime

from utils.build_embed import build_embed
from utils.music_handling.search_yt import search_yt
from utils.command_log import command_log
from utils.phrases.phrases import *

from utils.singletons.song_queue_singleton import SongQueue
from utils.singletons.vc_singleton import VC
from utils.singletons.options_singleton import Options
from utils.music_handling.play_music import play_music

from write_log import write_log

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.slash = SlashCommand(self.client, sync_commands=True)

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
    async def play(self, ctx: SlashContext, *args):
        command_log("play", ctx)
        write_log(False, f'{ctx.author} tried to execute /play command')
        now = datetime.datetime.now()
        command_push_time = now.strftime("%H:%M:%S")

        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send(build_embed(self.client, random.choice(errorPhrases), "Нелзя слушать музыку с закрытыми ушами!", discord.Color.red, True, False))
            write_log(False, f'/play command, pushed by {ctx.author}, was not executed (Not in the voice channel)')
        else:
            song = search_yt(Options().YTDL_OPTIONS, query)
            if type(song) == type(True):
                await ctx.send(build_embed(self.client, random.choice(playPhrases), f"Следующая на очереди: {song['title']}", discord.Color.orange, True, True, f"Заказал {ctx.author}"))
                write_log(False, f'{ctx.author}\'s /play command, pushed by him at {command_push_time}, was successfully executed')
            else:
                await ctx.send(build_embed(self.client, random.choice(queuePhrases), f"Прекрасная песня {song['title']} добавлена в наш список", discord.Color.orange, True, True, f"Заказал {ctx.author}"))
                write_log(False, f'{ctx.author}\'s /play command, pushed by him at {command_push_time}, was successfully executed')
                SongQueue().song_queue.append([song, voice_channel])
                write_log(False, f"{song['title']} was added to the queue")

                if self.is_playing is False:
                    await play_music(self.client, VC().vc, SongQueue().song_queue, Options().FFMPEG_OPTIONS)
