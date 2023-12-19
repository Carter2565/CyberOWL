import json
import base64
import Settings

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Reaction Remove module loading!¡!")

def event():
  def decorator(func):
    command_name = func.__name__  # Get the function name as the command name
    Settings.Functions.ReactRolesRemove[command_name] = func
    return func
  return decorator

@bot.event
async def on_raw_reaction_remove(reaction):
  for command_name in Settings.Functions.ReactRolesRemove:
    func = Settings.Functions.ReactRolesRemove[command_name]
    await func(reaction)
