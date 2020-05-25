import discord
import os
import config
import youtube_dl
import shutil
from os import system
from discord import utils
from discord.utils import get
from discord.ext import commands

bot = commands.Bot(command_prefix=config.PREFIX)

@bot.event
async def on_ready():
    print(f'{bot.user} is online')

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
        await ctx.send(f'О, {ctx.message.author.mention}, какая встреча!')
    else:
        voice = await channel.connect()

@bot.command(pass_context=True, aliases=['l', 'leav'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send('Удачи!')
    else:
        await ctx.send('Не могу уйти. Что-то пошло не так...')

@bot.command(pass_context=True, aliases=['p', 'pl'])
async def play(ctx, url : str):

    def check_queue():
        Queue_infile = os.path.isdir('./Queue')
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath('Queue'))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print('No more queued songs')
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath('Queue') + '\\' + first_file)
            if length != 0:
                song_there = os.path.isfile('song.mp3')
                if song_there:
                    os.remove('song.mp3')
                shutil.move(song_path, main_location)
                for file in os.listdir('./'):
                    if file.endswith('.mp3'):
                        os.rename(file, 'song.mp3')
                
                voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07
            else:
                queues.clear()
                return
        else:
            queues.clear()

    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            queues.clear()
    except PermissionError:
        print('Trying to delete the file but its being played...')
        return

    Queue_infile = os.path.isdir('./Queue')
    try:
        Queue_folder = './Queue'
        if Queue_infile is True:
            print('Removed old Queue folder')
            shutil.rmtree(Queue_folder)
    except:
        print('No old Queue folder')
    
    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format' : 'bestaudio/best',
        'quiet' : True,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print('FALLBACK: youtube-dl does not support this URL')
        c_path = os.path.dirname(os.path.realpath(__file__))
        system('spotdl -f ' + '"' + c_path + '"' + ' -s ' + url)
        
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            os.rename(file, 'song.mp3')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    try:
        nname = name.rsplit('—', 2)
        await ctx.send(f'Музыкальная ночь продолжается! Следующая песня — {nname[0]}')
    except:
        await ctx.send(f'Музыкальная ночь продолжается! Следующая песня — {nname[0]}')

@bot.command(pass_context=True)
async def pause(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.pause()
        await ctx.send('Подождать так подождать')
    else:
        await ctx.send('Молчание можно прервать только разговором')

@bot.command(pass_context=True)
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        voice.resume()
        await ctx.send('С радостью!')
    else:
        await ctx.send('Молчание можно прервать только разговором')

@bot.command(pass_context=True)
async def stop(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

    queue_infile = os.path.isdir('./Queue')
    if queue_infile is True:
        shutil.rmtree('./Queue')

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send('Сворачиваемся!')
    else:
        await ctx.send('Молчание можно прервать только разговором')

queues = {}

@bot.command(pass_context=True)
async def queue(ctx, url : str):
    Queue_infile = os.path.isdir('./Queue')
    if Queue_infile is False:
        os.mkdir('./Queue')
    DIR = os.path.abspath(os.path.realpath('Queue'))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num
    
    queue_path = os.path.abspath(os.path.realpath('Queue') + f'\song{q_num}.%(ext)s')

    ydl_opts = {
        'format' : 'bestaudio/best',
        'quiet' : True,
        'outtmpl' : queue_path,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        print('FALLBACK: youtube-dl does not support this URL')
        q_path = os.path.abspath(os.path.realpath('Queue'))
        system(f'spotdl -ff song{q_num} -f ' + '"' + q_path + '"' + ' -s ' + url)

    await ctx.send('Договорились :)')

@bot.command(pass_context=True)
async def skip(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        voice.stop()
        await ctx.send('Двигаемся дальше!')
    else:
        await ctx.send('Молчание можно прервать только разговором')

bot.run(config.TOKEN)