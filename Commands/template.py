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

print("[Python Bot] -- !¡!Command Loading!¡!")

@bot.command(aliases=[])
async def command(ctx):
  pass

print("[Python Bot] -- !¡!Command Loaded!¡!")
