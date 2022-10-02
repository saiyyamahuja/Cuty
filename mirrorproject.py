import os
import discord
from discord.enums import ContentFilter
#import typing as t
from discord.ext import commands
#from discord.ext.commands import Bot
import urllib.request
import re
import youtube_dl
import mysql.connector as ms

client=commands.Bot(command_prefix="xd ")
final_url=str()

'''@client.event
async def on_ready():
  print(f"Logged in as {client.user}")'''

'''mydb=ms.connect(host='*****',user='****',password='*******')
cursor=mydb.cursor()
traverse="SELECT * FROM TABLE slangs"
slangs=list(cursor.execute(traverse))'''

@client.event
async def on_ready():
    print("Bot is online")

async def on_disconnect():
    print("Bot if offline")

            
@client.event
async def on_raw_reaction_add(payload):
    message_id=payload.message_id
    target_message_id=894248995491303464
    guild_id=payload.guild_id
    guild = client.get_guild(guild_id)

    if message_id==target_message_id:
        if payload.emoji.name=="👨‍🎓":
            role=discord.utils.get(guild.roles, name="Student")
            await payload.member.add_roles(role)
        elif  payload.emoji.name=="👩‍🎓":
            role=discord.utils.get(guild.roles, name="Student")
            await payload.member.add_roles(role)
        elif payload.emoji.name=="🧑‍🏫":
            role=discord.utils.get(guild.roles, name="Teacher")
            await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    message_id=payload.message_id
    target_message_id=894248995491303464
    guild_id=payload.guild_id
    guild = client.get_guild(guild_id)

    if message_id==target_message_id:
        member=discord.utils.find(lambda m:m.id==payload.user_id, guild.members)
        if payload.emoji.name=="👨‍🎓":
            role=discord.utils.get(guild.roles, name="Student")
            await member.remove_roles(role)
        elif  member.emoji.name=="👩‍🎓":
            role=discord.utils.get(guild.roles, name="Student")
            await member.remove_roles(role)
        elif payload.emoji.name=="🧑‍🏫":
            role=discord.utils.get(guild.roles, name="Teacher")
            await member.remove_roles(role)
'''            
@client.event
async def on_message(message):
    content=message.content.split(" ")
    for i in content:
        for j in slangs:
            if i==j:
                await message.delete()
                author=ctx.author.id()
                auth_count=cursor.execute("SELECT count FROM slangs WHERE member_id=%s", (author))
                add="UPDATE slangs SET count=count+1 WHERE member_id= %s"
                if auth_count>2:
                    await message.channel.send("Please refrain from using abusive words.")
                    await ctx.author.ban(reason="abusing channel") # replace ban with kick or mute for kicking or muting member
                cursor.execute(add, (author))
'''
@client.command()
async def hello(ctx):   
    await ctx.send(ctx.author)
    await ctx.send(ctx.message)
    await ctx.send(ctx.guild)
    
@client.command()
@commands.has_permissions(permissions.kick_members)
async def kick(ctx, member:discord.Member,*, reason):
    await member.kick(reason=reason)
    
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")

@client.command()
@commands.has_permissions(permissions.ban_members)   
async def ban(ctx, member:discord.Member,*, reason):
    await member.ban(reason=reason)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")
    

@client.command()
@commands.has_permissions(permissions.ban_members)
async def unban(ctx, *,member):
    banned_members=await ctx.guild.bans()
    for person in banned_members:
        user=person.user
        if member==str(user):
            await member.unban(user)
            
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")


@client.command()
@commands.has_permissions(permissions.mute_members)
async def mute(ctx, *,member):
    await member.mute()
    
@mute.error
async def mute(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You do not have permission to use this command.")


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
      await message.channel.send(f"Requested by: @{message.author.mention}")
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
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@play.error
async def play_error(ctx,error):
  if isinstance(error,commands.CommandInvokeError):
      await ctx.send("I am not even in a voice channel!")

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