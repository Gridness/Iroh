import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class Repeat(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Repeat(client))

    @cog_ext.cog_slash(
        name="repeat",
        description="Если захочешь еще :)"
    )
    async def repeat(self, ctx: SlashContext):
        pass