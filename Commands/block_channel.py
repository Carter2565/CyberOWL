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

@bot.command(aliases=['block'])
async def block_channel(ctx, channel_id: int):
  channel = ctx.channel
  guild = channel.guild
  
  if not guild.id:
    pass
  else:
    isAdmin = any(role.permissions.administrator for role in ctx.author.roles)
    if isAdmin:
      try:
        with open("blocked_channels.json", "r+") as file:
          blocked_channels = json.load(file)
          if channel_id in blocked_channels:
            blocked_channels.remove(channel_id)
            await ctx.send(f"Channel {channel_id} has been unblocked.")
          else:
            blocked_channels.append(channel_id)
            await ctx.send(f"Channel {channel_id} has been blocked.")
          file.seek(0)
          json.dump(blocked_channels, file, indent=2)
      except FileNotFoundError:
        blocked_channels = [channel_id]
        with open("blocked_channels.json", "w") as file:
          json.dump(blocked_channels, file, indent=2)
        await ctx.send(f"Channel {channel_id} has been blocked.")
    else:
      await ctx.send('You must be a admin in the server')
