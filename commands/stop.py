import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class Stop(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Stop(client))

    @cog_ext.cog_slash(
        name="stop",
        description="Остановочка"
    )
    async def stop(self, ctx: SlashContext):
        pass