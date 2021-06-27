import discord
from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.phrases import *

class Resume(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Resume(client))

    @cog_ext.cog_slash(
        name="resume",
        description="Время продолжать"
    )
    async def resume(self, ctx: SlashContext):
        await ctx.voice_client.resume()
        await ctx.send(build_embed(self.client, "Продолжаем!", "Давно пора :)", discord.Color.orange, False, True, str(self.client.user)))