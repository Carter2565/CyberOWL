# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings
import Utils.HelpBook as HelpBook

# Import dependencies
import json
import base64
import re

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Help Command Loading!¡!")

class tools:
  @staticmethod
  async def embed(title, description, author=None, authorUrl=None, authorIconUrl=None, url=None,
                  color=discord.Color.blue()):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    if author or authorUrl or authorIconUrl:
      embed.set_author(name=author, url=authorUrl, icon_url=authorIconUrl)
    return embed

@bot.command(aliases=['h'])
async def help(ctx):
  Settings.helpPage = 0
  channel_id = ctx.channel.id
  with open("blocked_channels.json", "r+") as file:
    blocked_channels = json.load(file)
    if channel_id in blocked_channels:
      pass
    else:
      buttonHome = discord.ui.Button(label="<<", style=discord.ButtonStyle.secondary)
      buttonBack = discord.ui.Button(label="<", style=discord.ButtonStyle.secondary)
      buttonForward = discord.ui.Button(label=">", style=discord.ButtonStyle.secondary)
      buttonEnd = discord.ui.Button(label=">>", style=discord.ButtonStyle.secondary)

      class HelpView(discord.ui.View):
        def __init__(self):
          super().__init__()
          self.home_button = buttonHome
          self.back_button = buttonBack
          self.forward_button = buttonForward
          self.end_button = buttonEnd

      async def buttonHomeCallback(interaction):
        Settings.helpPage = 0
        await interaction.response.defer()
        await interaction.message.edit(
          embed=await tools.embed('Help Pg:' + str(Settings.helpPage + 1),
                                  HelpBook.commands[0] + '\n' + HelpBook.commands[Settings.helpPage + 1],
                                  color=discord.Color.red()))

      async def buttonBackCallback(interaction):
        Settings.helpPage -= 1
        if Settings.helpPage <= 0:
          Settings.helpPage = 0
        await interaction.response.defer()
        await interaction.message.edit(
          embed=await tools.embed('Help Pg:' + str(Settings.helpPage + 1),
                                  HelpBook.commands[0] + '\n' + HelpBook.commands[Settings.helpPage + 1],
                                  color=discord.Color.red()))
      
      async def buttonForwardCallback(interaction):
        Settings.helpPage += 1
        if Settings.helpPage >= (len(HelpBook.commands) - 2):
          Settings.helpPage = (len(HelpBook.commands) - 2)
        await interaction.response.defer()
        await interaction.message.edit(
          embed=await tools.embed('Help Pg:' + str(Settings.helpPage + 1),
                                  HelpBook.commands[0] + '\n' + HelpBook.commands[Settings.helpPage + 1],
                                  color=discord.Color.red()))

      async def buttonEndCallback(interaction):
        Settings.helpPage = (len(HelpBook.commands) - 2)
        await interaction.response.defer()
        await interaction.message.edit(
          embed=await tools.embed('Help Pg:' + str(Settings.helpPage + 1),
                                  HelpBook.commands[0] + '\n' + HelpBook.commands[Settings.helpPage + 1],
                                  color=discord.Color.red()))

      buttonHome.callback = buttonHomeCallback
      buttonBack.callback = buttonBackCallback
      buttonForward.callback = buttonForwardCallback
      buttonEnd.callback = buttonEndCallback

      view = HelpView()
      view.add_item(buttonHome)
      view.add_item(buttonBack)
      view.add_item(buttonForward)
      view.add_item(buttonEnd)

      await ctx.send(
        embed=await tools.embed(
          'Help',
          HelpBook.commands[0] + '\n' + HelpBook.commands[Settings.helpPage + 1],
          color=discord.Color.red()),
        view=view
        )

print("[Python Bot] -- !¡!Help Command Loaded!¡!")
