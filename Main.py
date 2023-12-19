import Settings
import logging

bot = Settings.Constructor.bot

# Set discord.py logging level to ERROR
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.ERROR)
discord_logger

@bot.event
async def on_ready():
  print('[Python Bot] -- {0.user} is online!'.format(bot))
  import Setup
  print("[Python Bot] -- !¡!Loading Modules!¡!") 
  print("-------------------------------------") 
  import Commands
  import Events
  import Levels
  import AutoMod.AutoMod
  print("[Python Bot] -- !¡!Modules Loaded!¡! ") 
  print("-------------------------------------") 

bot.run(Settings.Tokens.bot)
