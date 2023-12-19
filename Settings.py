# These are the settings for the bot
operator = '-'
helpPage = 0
updater = True
userdata = {}
admin = ["carter2565#0",]

class Tokens:
  bot = ''  

class Constructor:
  import discord
  from discord.ext import commands
  bot = commands.Bot(command_prefix=operator, intents=discord.Intents.all(), help_command=None)

class Functions:
  OnMessage = {}
  OnReactionAdd = {}
  ReactRolesRemove = {}
