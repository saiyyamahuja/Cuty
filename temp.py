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

@client.event
async def on_message(message):

    await message.channel.send(f"<@644126548818919434> has been kicked from the server")
    await message.channel.send("Please refrain from using abusive words")
    await message.author.ban("abusing channel")
client.run('ODc2NzY3NzAxNzE5MTk1NjQ5.YRo3jQ.FrECKz012SvpoZ4IahzkJqUKYn8')