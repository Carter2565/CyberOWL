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

print("[Python Bot] -- !¡!Get Reactions Command Loading!¡!")

@bot.command() 
async def get_reactions(ctx, Channel: int, Message: int): # (Channel ID, Message ID)
  channel_id = ctx.channel.id
  with open("blocked_channels.json", "r+") as file:
    blocked_channels = json.load(file)
    if channel_id in blocked_channels:
      pass
    else:
      try:
        channel = await bot.fetch_channel(Channel)
        try:
          fetched_message = await channel.fetch_message(Message)

          reactions = fetched_message.reactions
          reaction_dict = {}

          for reaction in reactions:
            count = reaction.count
            emoji = reaction.emoji

            users = []
            async for user in reaction.users():
              users.append(user.name)

            reaction_dict[str(emoji)] = set(users)

          for emoji, users in reaction_dict.items():
            user_list = ', '.join(users)
            await ctx.send(f'{emoji}: {user_list} ({len(users)} total)')
        except discord.errors.HTTPException:
          await ctx.send("Can't find Message")
      except discord.errors.HTTPException:
        await ctx.send("Can't find Channel")

print("[Python Bot] -- !¡!Get Reactions Command Loaded!¡!")
