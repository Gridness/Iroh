from discord.ext import commands, tasks
import datetime
from write_log import write_log

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    def setup(client):
        client.add_cog(Ping(client))

    @tasks.loop(seconds=60.0)
    async def get_ping(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f'[{current_time}] Ping: {round(self.client.latency * 1000, 2)} ms')
        write_log(False, f'Ping: {round(self.client.latency * 1000, 2)} ms')