import discord
from utils.singletons.song_queue_singleton import SongQueue
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class NowPlaying(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(NowPlaying(client))

    @cog_ext.cog_slash(
        name="now",
        description="Хочешь узнать, под что сейчас пляшем?"
    )
    async def now_playing(self, ctx: SlashContext):
        await ctx.send(build_embed(self.client, "Сейчас играет", SongQueue().song_queue[0][0]['title'], discord.Color.orange, False, False))