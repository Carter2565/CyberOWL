# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings

# Import dependencies
import json
import asyncio

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Member Join event loading!¡!")

@bot.event
async def on_presence_update(before, after):
  async def process_update():
    if after.status == discord.Status.online or after.status == discord.Status.offline:
      if Settings.updater:
        guild = after.guild
        with open("MemberCount.json", "r+") as file:
          MemberCount = json.load(file)

        if str(guild.id) not in MemberCount:
          return

        for count_channel in MemberCount[str(guild.id)]:
          channel_id = MemberCount[str(guild.id)][count_channel]['ID']
          channel_name = MemberCount[str(guild.id)][count_channel]['NAME']

          channel = guild.get_channel(channel_id)
          
          try:
            if count_channel == 'OnlineCount':
              online_members = sum(member.status == discord.Status.online for member in guild.members)
              old_online = channel.name.split(channel_name)[1]
              if int(old_online) != online_members:
                await channel.edit(name=f'{channel_name}{online_members}')
            if count_channel == 'OfflineCount':
              offline_members = sum(member.status == discord.Status.offline for member in guild.members)
              old_offline = channel.name.split(channel_name)[1]
              if int(old_offline) != offline_members:
                await channel.edit(name=f'{channel_name}{offline_members}')
          except AttributeError:  # A channel was deleted without deleting from bot config
            pass
          except discord.HTTPException as e:
            if e.status == 429:  # Rate limit error
              print("Rate limited. Passing")
              return
  try:
    await asyncio.wait_for(process_update(), timeout=5)  # Timeout set to 5 seconds
  except asyncio.TimeoutError:
    print("Update processing failed due to timeout! This is probably due to a rate limit")
    pass 
