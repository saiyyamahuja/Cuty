import os
import discord
from discord.enums import ContentFilter
#import typing as t
from discord.ext import commands
#from discord.ext.commands import Bot
import urllib.request
import re
import youtube_dl

client=commands.Bot(command_prefix="xd ")
final_url=str()

'''@client.event
async def on_ready():
  print(f"Logged in as {client.user}")'''

@client.command()
async def join(ctx):
  channel=ctx.author.voice.channel
  await channel.connect()

@join.error
async def join_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("Join a voice channel to use this command!")

@client.command()
async def disconnect(ctx):
  channel = ctx.voice_client
  await channel.disconnect()

@disconnect.error
async def disconnect_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")



@client.event
async def on_message(message):
  
  mssg = message.content
  if message.author==client:
    return
  if mssg.lower().startswith("xd"):
    mssg=mssg.lower()
    list_mssg=mssg.split(" ")
    if list_mssg[1] in "play":
      del list_mssg[0]
      del list_mssg[0]
      a=str()
      for i in list_mssg:
        a+= i+ "+"
      search_url="https://www.youtube.com/results?search_query="+a
      html = urllib.request.urlopen(search_url)
      video_urls=re.findall(r"watch\?v=(\S{11})", html.read().decode())
      global final_url
      final_url="https://www.youtube.com/watch?v="+video_urls[0]
      await message.channel.send(final_url)
      await message.channel.send(f"Requested by: @{message.author}")
  await client.process_commands(message)
      

@client.command()
async def play(ctx, url:str):


    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current song to end.")
        return
 
    voice = ctx.voice_client
    url = final_url
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3",executable='ffmpeg'))

'''@play.error
async def play_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")'''

@client.command()
async def pause(ctx):
  voice=ctx.voice_client
  if voice.is_playing():
        voice.pause()
  else:
        await ctx.send("I am not even talking dude!")

@pause.error
async def pause_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")

@client.command()
async def resume(ctx):
  voice=ctx.voice_client
  if voice.is_paused():
        voice.resume()
  else:
        await ctx.send("The audio is not paused!")

@resume.error
async def resume_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")

@client.command()
async def stop(ctx):
  voice=ctx.voice_client
  if voice.is_playing():
        voice.stop()
  else:
        await ctx.send("I am mummmm :-)")

@stop.error
async def stop_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")






client.run('ODc2NzY3NzAxNzE5MTk1NjQ5.YRo3jQ.FrECKz012SvpoZ4IahzkJqUKYn8')