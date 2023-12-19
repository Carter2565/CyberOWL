import Events.on_message as OnMessage
import Settings
import json
import discord
import time
import datetime
import asyncio

bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Auto Mod module loading!¡!")
print("[Python Bot] -- !¡!Spam Filter module loading!¡!")

message_counts = {}
last_user = bot.user.id
last_reset_time = time.time()

@OnMessage.event()
async def SpamFilter(message):
  global last_user
  # Check if the message is from a bot or in a different channel (customize this logic if needed)
  if message.author.bot or isinstance(message.channel, discord.DMChannel):
    return

  # Track message counts per user
  author_id = message.author.id
  if author_id not in message_counts:
    message_counts[author_id] = 1
  else:
    message_counts[author_id] += 1

  # Define spam threshold (adjust as needed)
  spam_threshold = 3

  global last_reset_time
  message_time = time.time() - last_reset_time
  if (message_time > 10) or not (last_user == author_id):
    message_counts[author_id] = 0
    last_reset_time = time.time()

  if message_counts[author_id] > spam_threshold:
    await message.author.timeout(datetime.timedelta(seconds=7))
    responce = await message.channel.send(f"{message.author.mention}, please avoid spamming! \nIf your not, please send longer messages rather than many messages")
    await message.delete()
    await asyncio.sleep(8)
    await responce.delete()

  last_user = author_id
  await bot.process_commands(message)
  
print("[Python Bot] -- !¡!Mass Filter module loading!¡!")
  
mass_message_counts = {}
mass_last_reset_time = time.time()

# @OnMessage.event()
async def Massfilter(message):
  # Check if the message is from a bot or in a different channel (customize this logic if needed)
  if message.author.bot or isinstance(message.channel, discord.DMChannel):
    return

  # Track message counts per user
  author_id = message.author.id
  if author_id not in mass_message_counts:
    mass_message_counts[author_id] = 1
  else:
    mass_message_counts[author_id] += 1

  # Define spam threshold (adjust as needed)
  spam_threshold = 7

  global mass_last_reset_time
  message_time = time.time() - mass_last_reset_time
  if (message_time > 60):
    mass_message_counts[author_id] = 0
    mass_last_reset_time = time.time()

  if mass_message_counts[author_id] > spam_threshold:
    await message.author.timeout(datetime.timedelta(seconds=10))
    responce = await message.channel.send(f"{message.author.mention}, please avoid mass messages! \nPlease send longer messages rather than many messages")
    await message.delete()
    await asyncio.sleep(15)
    await responce.delete()

print("[Python Bot] -- !¡!Auto Mod module loaded!¡!")
print("-------------------------------------") 