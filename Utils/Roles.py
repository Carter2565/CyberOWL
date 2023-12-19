import json
import discord

async def add_role_by_id(client, guild_id: int, member_id: int, role_name: str):
  guild = await client.fetch_guild(guild_id)
  if guild:
    member = await guild.fetch_member(member_id)
    if member:
      role = discord.utils.get(guild.roles, name=role_name)
      if role:
        if not any(role.permissions.administrator for role in member.roles): # This dissables reaction roles for server admin
          await member.add_roles(role)
          print(f"[Python Bot] - [Roles.py] - Role {role.name} added to {member.display_name}.")  # Debug
        else:
          print(f"[Python Bot] - [Roles.py] - {member.display_name} is a server admin!")
      else:
        print(f"[Python Bot] - [Roles.py] - Role {role_name} not found.")
    else:
      print(f"[Python Bot] - [Roles.py] - Member with ID {member_id} not found.")
  else:
    print(f"[Python Bot] - [Roles.py] - Guild with ID {guild_id} not found.")

async def remove_role_by_id(client, guild_id: int, member_id: int, role_name: str):
  guild = await client.fetch_guild(guild_id)
  if guild:
    member = await guild.fetch_member(member_id)
    if member:
      role = discord.utils.get(guild.roles, name=role_name)
      if role:
        if not any(role.permissions.administrator for role in member.roles): # This dissables reaction roles for server admin
          await member.remove_roles(role)
          print(f"[Python Bot] - [Roles.py] - Role {role.name} removed from {member.display_name}.")  # Debug
        else:
          print(f"[Python Bot] - [Roles.py] - {member.display_name} is a server admin!")
      else:
        print(f"[Python Bot] - [Roles.py] - Role {role_name} not found.")
    else:
      print(f"[Python Bot] - [Roles.py] - Member with ID {member_id} not found.")
  else:
    print(f"[Python Bot] - [Roles.py] - Guild with ID {guild_id} not found.")