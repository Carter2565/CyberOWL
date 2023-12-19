# Import Discord 
import discord
from discord.ext import commands

# Import dependencies
import random

# Import Local files
import Settings
import Events.on_message as OnMessage
import Events.on_raw_reaction_add as OnReactionAdd

# Import the bot constructor
bot = Settings.Constructor.bot

class tools:
  @staticmethod
  def embed(title: None, description: None, author=None, authorUrl=None, authorIconUrl=None, url=None,
                  color=discord.Color.blue()):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    if author or authorUrl or authorIconUrl:
      embed.set_author(name=author, url=authorUrl, icon_url=authorIconUrl)
    return embed

def check_emoji(guild_id):
  guild = bot.get_guild(guild_id)
  emoji_name = 'CyberBit'
  
  # Check if the emoji exists in the guild
  existing_emoji = discord.utils.get(guild.emojis, name=emoji_name)
    
  if existing_emoji:
    return True
  else:
    # Check available emoji slots
    emoji_limit = guild.emoji_limit
    emojis_count = len(guild.emojis)
    
    if emojis_count < emoji_limit:
      # Upload the emoji
      with open('./CyberBit.png', 'rb') as image:
        emoji_bytes = image.read()
      guild.create_custom_emoji(name=emoji_name, image=emoji_bytes)
      return True
    else:
      return False

def create_profile(user):
  embed = tools.embed(
    None,
    f''':military_medal: | Level {user['level']}
:star: | {user['stars']} stars
:speech_balloon: | {user['messages']} messages sent
:microphone2: | {user['voice']} in voice
{':CyberBit:' if check_emoji(user['guild']) else ':coin:'} | {user['bits']} CyberBits
    ''',
    author=f"<@{user['id']}>'s Profile",
    authorIconUrl=bot.get_user(user['id']).avatar.url,
    color=discord.Color.red()
  )
  return embed

async def give_xp(user_id, guild_id, xp_earned):
  if guild_id not in Settings.userdata:
    Settings.userdata[guild_id] = {}
  user_data = Settings.userdata[guild_id]
  if user_id not in user_data:
    user_data[user_id] = {
      'id':user_id,
      'guild': guild_id,
      'level': 0,
      'stars': 0,
      'messages': 0,
      'voice': 0,
      'xp': 0,
      'bits': 0,
    }
 


  user = user_data[user_id]
  user['xp'] += xp_earned

  # Define the logic for leveling up
  xp_needed = 10 if user['level'] < 2 else 10 * user['level']
  if user['xp'] >= xp_needed:
    user['level'] += 1
    user['xp'] -= xp_needed
    if 'Channel' in Settings.userdata[guild_id]:
      if Settings.userdata[guild_id]['Channel']:
        channel = bot.fetch_channel(Settings.userdata[guild_id]['Channel'])
        channel.send(f'<@{user_id}> Just Leveled Up!')
        await channel.send(
          embed=create_profile(user)
        )

  # Modify leveling speed for different levels
  # For instance, lower levels might require less XP to level up
  if user['level'] != 0:
    level_factor = 1 / user['level']  # Adjust this factor to control leveling speed
  else: 
    level_factor = 1
  user['xp'] += xp_earned * level_factor


# '▰' ▱