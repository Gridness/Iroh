from discord.ext import commands
from discord_slash import SlashContext, cog_ext

from utils.build_embed import build_embed
from utils.command_log import command_log
from utils.phrases import *

from utils.singletons.song_queue_singleton import SongQueue

class Queue(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Queue(client))

    @cog_ext.cog_slash(
        name="queue",
        description="Все музыкальные услады этого вечера"
    )
    async def queue(self, ctx: SlashContext):
        command_log("queue", ctx)

        retval = ""
        for i in range(0, len(SongQueue().song_queue)):
            retval += SongQueue().song_queue[i][0]['title'] + "\n"

        print(retval)
        if retval != "":
            await ctx.send(build_embed())
        else:
            await ctx.send(build_embed())