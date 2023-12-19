import json
import base64
import Settings
import Events.on_raw_reaction_add as OnReactionAdd 
from Utils.Roles import *

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!React Roles Add module loading!¡!")

@OnReactionAdd.event()
async def ReactRolesAdd(reaction):
  with open("ReactRoles.json", "r+") as file:
    ReactRoles = json.load(file)

  # Gets the IDS
  channel_id = reaction.channel_id
  message_id = reaction.message_id
  user_id = reaction.user_id

  # Get the relevant objects using the IDs
  channel = bot.get_channel(channel_id)
  message = await channel.fetch_message(message_id)
  user = await bot.fetch_user(user_id)

  # Get the server ID
  server_id = message.guild.id

  emoji = base64.b64encode(str(reaction.emoji).encode("utf-8")).decode("utf-8")
  print(f'{reaction.emoji.name} - {emoji} - Config only')

  if str(server_id) in ReactRoles:
    if str(channel_id) in ReactRoles[str(server_id)]:
      if str(message_id) in ReactRoles[str(server_id)][str(channel_id)]:
        if (f'{reaction.emoji.name}' in ReactRoles[str(server_id)][str(channel_id)][str(message_id)]):
          # Imported from roles.
          await add_role_by_id(bot,server_id,user.id,ReactRoles[str(server_id)][str(channel_id)][str(message_id)][str(reaction.emoji.name)])
        elif(f'{emoji}' in ReactRoles[str(server_id)][str(channel_id)][str(message_id)]):
          # Imported from roles.
          await add_role_by_id(bot,server_id,user.id,ReactRoles[str(server_id)][str(channel_id)][str(message_id)][emoji])

  # print(f'{user} added reaction {emoji} to message {message}')