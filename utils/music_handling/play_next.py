import discord
from commands.play import Music

def play_next(vc, song_queue, FFMPEG_OPTIONS):
    if len(song_queue) > 0:
        Music.is_playing = True
        extracted_url = song_queue[0][0]['source']
        song_queue.pop(0)
        vc.play(discord.FFmpegAudio(extracted_url, **FFMPEG_OPTIONS), after=lambda e: play_next())
    else:
        Music.is_playing = False