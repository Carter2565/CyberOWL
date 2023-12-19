# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings
from Levels.leveler import create_profile

# Import dependencies
import json
import base64
import re

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Profile Command Loading!¡!")

@bot.command(aliases=['pf'])
async def profile(ctx, user = None):
  if user == None:
    user_id = ctx.author.id
  elif user.isdigit():  # Check if it's a numeric user ID
    user_id = user
  elif isinstance(user, str):  # Check if it's a string
    user_id = int(re.search(r'\d+', user).group())
  guild_id = ctx.guild.id
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
  await ctx.send(embed = create_profile(user_data[user_id]))

print("[Python Bot] -- !¡!Profile Command Loaded!¡!")
