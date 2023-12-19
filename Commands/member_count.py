# Import Discord 
import discord
from discord.ext import commands

# Import Local files
import Settings
from Utils import MemberCount as MC

# Import dependencies
import json

# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!Member Count Command Loading!¡!")

@bot.command(aliases=['members'])
async def member_count(ctx, config: str = False, arg: str = None):
  def check(m):
    return m.author == ctx.author
  
  if ctx.guild:
    guild = ctx.guild

    if guild:
      try:
        user = await guild.fetch_member(ctx.author.id)
      except discord.NotFound:
        return await ctx.send("You're not a member of this guild.")
      except discord.HTTPException:
        return await ctx.send("Failed to fetch your info. Please try again.")

      if user:
        member_count = guild.member_count
        await ctx.send(f"Total members in {guild.name}: {member_count}")
        # Check if the user has admin permissions
        if any(role.permissions.administrator for role in user.roles):
          if config:
            yes = ['y','yes']
            no = ['n','no']
            exit = ['esc','exit']
            
            async def MemberCount():
              await ctx.send("Do you want to add/modify a total members count?")
              response = await bot.wait_for('message', check=check)#, timeout=30)
              
              _ = True
              while _:
                if response.content.lower() in  yes: # Member Count
                  await ctx.send("Do you want to set a custom channel name?")
                  response = await bot.wait_for('message', check=check)#, timeout=30)
                  
                  __ = True
                  while __:
                    if response.content.lower() in  yes: # Member Count Naming
                      __ = False
                      await ctx.send("What is the name you want to set a custom channel name?")
                      response = await bot.wait_for('message', check=check)#, timeout=30)
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                      
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['MemberCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel(f'{response.content}: ')
                        await vc.edit(name=f'{response.content}: ')
                      except KeyError:
                        vc = await guild.create_voice_channel(f'{response.content}: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['MemberCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['MemberCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in no: # Member Count Naming
                      __ = False
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                        
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['MemberCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel('Members: ')
                      except KeyError:
                        vc = await guild.create_voice_channel('Members: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['MemberCount'] = {
                            "ID": vc.id,
                            'NAME': 'Members: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['MemberCount'] = {
                            "ID": vc.id,
                            'NAME': 'Members: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in exit: # Member Count Naming
                      __ = False
                      return
                      pass
                    else: # Member Count Naming
                      await ctx.send('Please respond with Yes or No. To exit send exit')
                    _ = False
                    await ctx.send(f"The Member Count will update when config ends")
                elif response.content.lower() in no: # Member Count
                  _ = False
                  pass
                elif response.content.lower() in exit: # Member Count
                  _ = False
                  return
                  pass
                else: # Member Count
                  await ctx.send('Please respond with Yes or No. To exit send exit')
                
            async def OnlineCount():
              await ctx.send("Do you want to add a online members count?")
              response = await bot.wait_for('message', check=check)#, timeout=30)
              
              _ = True
              while _:
                if response.content.lower() in  yes: # Online Count
                  await ctx.send("Do you want to set a custom channel name?")
                  response = await bot.wait_for('message', check=check)#, timeout=30)
                  
                  __ = True
                  while __:
                    if response.content.lower() in  yes: # Online Count Naming
                      __ = False
                      await ctx.send("What is the name you want to set a custom channel name?")
                      response = await bot.wait_for('message', check=check)#, timeout=30)
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                      
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['OnlineCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel(f'{response.content}: ')
                        await vc.edit(name=f'{response.content}: ')
                      except KeyError:
                        vc = await guild.create_voice_channel(f'{response.content}: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['OnlineCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['OnlineCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in no: # Online Count Naming
                      __ = False
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                        
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['OnlineCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel('Online: ')
                      except KeyError:
                        vc = await guild.create_voice_channel('Online: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['OnlineCount'] = {
                            "ID": vc.id,
                            'NAME': 'Online: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['OnlineCount'] = {
                            "ID": vc.id,
                            'NAME': 'Online: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in exit: # Online Count Naming
                      __ = False
                      return
                      pass
                    else: # Online Count Naming
                      await ctx.send('Please respond with Yes or No. To exit send exit')
                    _ = False
                    await ctx.send(f"The Online Count will update when config ends")
                elif response.content.lower() in no: # Online Count
                  _ = False
                  pass
                elif response.content.lower() in exit: # Online Count
                  _ = False
                  return
                  pass
                else: # Online Count
                  await ctx.send('Please respond with Yes or No. To exit send exit')
                 
            async def OfflineCount():
              await ctx.send("Do you want to add a offline members count?")
              response = await bot.wait_for('message', check=check)#, timeout=30)
              
              _ = True
              while _:
                if response.content.lower() in  yes: # Offline Count
                  await ctx.send("Do you want to set a custom channel name?")
                  response = await bot.wait_for('message', check=check)#, timeout=30)
                  
                  __ = True
                  while __:
                    if response.content.lower() in  yes: # Offline Count Naming
                      __ = False
                      await ctx.send("What is the name you want to set a custom channel name?")
                      response = await bot.wait_for('message', check=check)#, timeout=30)
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                      
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['OfflineCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel(f'{response.content}: ')
                        await vc.edit(name=f'{response.content}: ')
                      except KeyError:
                        vc = await guild.create_voice_channel(f'{response.content}: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['OfflineCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['OfflineCount'] = {
                            "ID": vc.id,
                            'NAME': f'{response.content}: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in no: # Offline Count Naming
                      __ = False
                      
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        f.close()
                        
                      try:
                        vc = bot.get_channel(MemberCount[str(guild.id)]['OfflineCount']['ID'])
                        try: 
                          id = vc.id
                        except AttributeError:
                          vc = await guild.create_voice_channel('Offline: ')
                      except KeyError:
                        vc = await guild.create_voice_channel('Offline: ')
                        
                      with open('MemberCount.json', 'r+') as f:
                        MemberCount = json.load(f)
                        if str(guild.id) in MemberCount:
                          MemberCount[str(guild.id)]['OfflineCount'] = {
                            "ID": vc.id,
                            'NAME': 'Offline: '
                          }
                        else:
                          MemberCount[str(guild.id)] = {}
                          MemberCount[str(guild.id)]['OfflineCount'] = {
                            "ID": vc.id,
                            'NAME': 'Offline: '
                          }
                        f.close()
                      with open('MemberCount.json', 'w+') as f:
                        MemberCount = json.dump(MemberCount, f)
                        f.close()
                      pass
                    elif response.content.lower() in exit: # Offline Count Naming
                      __ = False
                      return
                      pass
                    else: # Offline Count Naming
                      await ctx.send('Please respond with Yes or No. To exit send exit')
                    _ = False
                    await ctx.send(f"The Online Count will update when config ends")
                elif response.content.lower() in no: # Offline Count
                  _ = False
                  pass
                elif response.content.lower() in exit: # Offline Count
                  _ = False
                  return
                  pass
                else: # Offline Count
                  await ctx.send('Please respond with Yes or No. To exit send exit')
                         
            if config.lower() in ['members']:
              await MemberCount()
              await ctx.send(f'Config Complete! Updating values')
            elif config.lower() in ['online']:
              await OnlineCount()
              await ctx.send(f'Config Complete! Updating values')
            elif config.lower() in ['offline']:
              await OfflineCount()
              await ctx.send(f'Config Complete! Updating values')
            elif config.lower() in ['update']:
              await ctx.send(f'Updating values \nIf we are rate limited the values wont update')
            else:
              await MemberCount()
              
              await OnlineCount()
              
              await OfflineCount()
            
              await ctx.send(f'Config Complete! Updating values')
              
            await MC.update(guild)
        else:
          await ctx.send("You must be an admin in the server to use this command.")
  else:
    await ctx.send('Please provide a guild id')


print("[Python Bot] -- !¡!Member Count Command Loaded!¡!")
