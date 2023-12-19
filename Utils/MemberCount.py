# Import Discord 
import discord

# Import Local files
import Settings

# Import dependencies
import json

# Import the bot constructor
bot = Settings.Constructor.bot 
  
async def update(guild):
  with open("MemberCount.json", "r+") as file:
    MemberCount = json.load(file)

  if str(guild.id) not in MemberCount:
    return

  for count_channel in MemberCount[str(guild.id)]:
    channel_id = MemberCount[str(guild.id)][count_channel]['ID']
    channel_name = MemberCount[str(guild.id)][count_channel]['NAME']

    channel = bot.get_channel(channel_id)
    
    try: 
      if count_channel == 'MemberCount':
        await channel.edit(name=f'{channel_name}{guild.member_count}')
      if count_channel == 'OnlineCount':
        online_members = sum(member.status == discord.Status.online for member in guild.members)
        await channel.edit(name=f'{channel_name}{online_members}')
      if count_channel == 'OfflineCount':
        offline_members = sum(member.status == discord.Status.offline for member in guild.members)
        await channel.edit(name=f'{channel_name}{offline_members}')
    except AttributeError: # A channel was deleted without deleting from bot config
      pass
