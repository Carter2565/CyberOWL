# Import Discord 
import discord
from discord.ext import commands

# Import dependencies
import random

# Import Local files
import Settings
from . import leveler
import Events.on_message as OnMessage
import Events.on_raw_reaction_add as OnReactionAdd


@OnMessage.event()
async def calculate_message_xp(message):
  xp_per_character = random.triangular(0.0005, 0.001, 0.0001)
  await leveler.give_xp(message.author.id, message.guild.id, len(message.content) * xp_per_character)

@OnReactionAdd.event()
async def calculate_reaction_xp(reaction):
  xp = random.triangular(0.05, 0.1, 0.0001)
  await leveler.give_xp(reaction.user_id, reaction.guild.id, xp)
