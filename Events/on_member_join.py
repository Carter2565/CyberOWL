# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings

# Import dependencies
import json

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Member Join event loading!¡!")

@bot.event
async def on_member_join(member):
  print(f'{member.global_name} Joined')
  with open("MemberCount.json", "r+") as file:
    MemberCount = json.load(file)

  if str(member.guild.id) not in MemberCount:
    return

  # server = task[str(server.id)]
  channel_id = MemberCount[str(member.guild.id)]['MemberCount']['ID']
  channel_name = MemberCount[str(member.guild.id)]['MemberCount']['NAME']

  channel = await member.guild.fetch_channel(channel_id)
  await channel.edit(name=f'{channel_name}{member.guild.member_count}')