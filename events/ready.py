from tasks.status_loop import Status
from tasks.ping import Ping
from discord.ext import commands
import json
import datetime
import os

from clean_log import clean_log
from write_log import write_log

class Ready(commands.Cog, name='Ready'):
    def __init__(self, client):
        self.client = client
        with open('F:\Vse\Bots\IrohBot\data.json', 'r') as data_file:
            self.data = json.load(data_file)

    def setup(client):
        client.add_cog(Ready(client))

    @commands.Cog.listener()
    async def on_ready(self):
        clean_log()
        now = datetime.datetime.now()
        clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clear_console()
        print(f'{self.data["meta"]["name"]} {self.data["meta"]["version"]} (c) {self.data["meta"]["dev"]} 2020 - {now.year}')
        print(f'{self.client.user} is online')
        write_log(True, 'Bot has been started')
        Ping.get_ping.start(self)
        Status.change_status.start(self)