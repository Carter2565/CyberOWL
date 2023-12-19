# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings

# Import dependencies
import json
import base64
import re

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Exit Command Loading!¡!")

@bot.command()
async def exit(ctx):
  channel_id = ctx.channel.id
  with open("blocked_channels.json", "r+") as file:
    blocked_channels = json.load(file)
    if channel_id in blocked_channels:
      pass
    else:
      if str(ctx.author) in Settings.admin:
        await ctx.send('Bot logging out!')
        await bot.close()
        exit()
      else:
        await ctx.send('You are not in the bot admin list, sorry')

  
print("[Python Bot] -- !¡!Exit Command Loaded!¡!")