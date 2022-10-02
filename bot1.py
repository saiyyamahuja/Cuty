import discord
import mysql.connector as ms
import commands.py as cm
client = discord.Client()

'''
mydb=ms.connect(host='*****',user='****',password='*******')
cursor=mydb.cursor()
traverse="SELECT * FROM TABLE slangs"
slangs=list(cursor.execute(traverse))
'''

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



client.run('ODkzMTkyNTQxNTUyNDAyNDky.YVX4YA.bGUJeoHkGJkr_HXsh11lElzhJNo')