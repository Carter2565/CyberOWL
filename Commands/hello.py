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

print("[Python Bot] -- !¡!Hello Command Loading!¡!")

@bot.command(aliases=['hi'])
async def hello(ctx):
  channel_id = ctx.channel.id
  with open("blocked_channels.json", "r+") as file:
    blocked_channels = json.load(file)
  if channel_id in blocked_channels:
    pass
  else:
    # await ctx.send(user)
    await ctx.send("Hello")

print("[Python Bot] -- !¡!Hello Command Loaded!¡!")