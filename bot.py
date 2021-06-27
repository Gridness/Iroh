"""
Iroh 4.0 © Gridness 2020 - 2021

This software is licensed under the MIT license
"""

from tasks.ping import Ping
from commands.play import Music
from commands.pause import Pause
from commands.resume import Resume
from tasks.status_loop import Status
from events.ready import Ready

from discord.ext import commands
import json

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

client = commands.Bot(command_prefix=None)

cogs = [Ready, Ping, Status, Music, Pause, Resume]
for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(data["token"])