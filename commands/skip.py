import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

from utils.singletons.song_queue_singleton import SongQueue
from utils.music_handling.play_music import play_music
from utils.singletons.vc_singleton import VC

class Skip(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Skip(client))

    @cog_ext.cog_slash(
        name="skip",
        description="Надоело? Перейдем к следующей!"
    )
    async def skip(self, ctx: SlashContext):
        if VC().vc != "":
            VC().vc.stop()
        else:
            await play_music(self.client, VC().vc, SongQueue().song_queue)