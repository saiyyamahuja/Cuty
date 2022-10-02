import discord
from changer import data,real_trouble

client = discord.Client()
data= data[0]

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



client.run('ODkzMTkyNTQxNTUyNDAyNDky.YVX4YA.bGUJeoHkGJkr_HXsh11lElzhJNo')