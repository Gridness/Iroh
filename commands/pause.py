import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class Pause(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Pause(client))

    @cog_ext.cog_slash(
        name="pause",
        description="Мы никуда не спешим, можем подождать :)"
    )
    async def pause(self, ctx: SlashContext):
        await ctx.voice_client.pause()
        await ctx.send(build_embed(self.client, "Пауза", "Подождем :)", discord.Color.orange, False, True, str(self.client.user)))