import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class Queue(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Queue(client))

    @cog_ext.cog_slash(
        name="queue",
        description="Мы никуда не спешим, можем подождать :)"
    )
    async def queue(self, ctx: SlashContext):
        pass