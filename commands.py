import discord
from discord.ext import commands
from discord import permissions
from discord.ext.commands.core import command
client = commands.Bot(command_prefix="!")

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

client.run('ODkzMTkyNTQxNTUyNDAyNDky.YVX4YA.JY1OURkEkReDbrGKDpFhu8tguoY')
