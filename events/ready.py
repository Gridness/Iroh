from tasks.status_loop import Status
from tasks.ping import Ping
from discord.ext import commands
import json
import datetime


class Ready(commands.Cog, name='Ready'):
    def __init__(self, client):
        self.client = client
        with open('F:\Vse\Bots\IrohBot\data.json', 'r') as data_file:
            self.data = json.load(data_file)

    def setup(client):
        client.add_cog(Ready(client))

    @commands.Cog.listener()
    async def on_ready(self):
        now = datetime.datetime.now()
        print(f'{self.data["meta"]["name"]} {self.data["meta"]["version"]} (c) {self.data["meta"]["dev"]} 2020 - {now.year}')
        print(f'{self.client.user} is online')
        Ping.get_ping.start(self)
        Status.change_status.start(self)