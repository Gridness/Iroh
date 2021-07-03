from utils.music_handling.play_next import play_next
import discord
from commands.play import Music

async def play_music(client, vc, song_queue, FFMPEG_OPTIONS):
    if len(song_queue) > 0:
        Music.is_playing = True
        
        extracted_url = song_queue[0][0]['source'] 
        if vc == "" or not not vc.is_connected():
            vc = await song_queue[0][1].connect()
        else:
            vc = await client.move_to(song_queue[0][1])
        print(song_queue)
        song_queue.pop(0)
        vc.play(discord.FFmpegAudio(extracted_url, **FFMPEG_OPTIONS), after=lambda e: play_next(vc, song_queue, FFMPEG_OPTIONS))
    else:
        Music.is_playing = False