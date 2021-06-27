from os import name
import discord
from discord.ext import commands, tasks
import random
import utils.status


class Status(commands.Cog, name='Status'):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Status(client))

    @tasks.loop(seconds=20.0)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(random.choice(utils.status.status)))