"""
Iroh 4.0 © Gridness 2020 - 2021

This software is licensed under the MIT license
"""

from commands.now_playing import NowPlaying
from commands.queue import Queue
from commands.skip import Skip
from commands.stop import Stop
from tasks.ping import Ping
from commands.play import Music
from commands.pause import Pause
from commands.resume import Resume
from tasks.status_loop import Status
from events.ready import Ready
# import os -> auto load all cogs (I'm just too stupid to do this)

from discord.ext import commands
import json

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

client = commands.Bot(command_prefix="!")

cogs = [Ready, Ping, Status, Music, Pause, Resume, Stop, Skip, Queue, NowPlaying]

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(data["token"])