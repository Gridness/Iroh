from utils.is_playing_state_singleton import IsPlaying
import discord

def play_next(vc, song_queue, FFMPEG_OPTIONS):
    if len(song_queue) > 0:
        IsPlaying().is_paying = True
        extracted_url = song_queue[0][0]['source']
        song_queue.pop(0)
        vc.play(discord.FFmpegAudio(extracted_url, **FFMPEG_OPTIONS), after=lambda e: play_next())
    else:
        IsPlaying().is_paying= False