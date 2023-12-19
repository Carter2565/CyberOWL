import os
import json
import base64
import Settings
from Utils.Roles import *

# Import the bot constructor
bot = Settings.Constructor.bot

print("-------------------------------------")
print("[Python Bot] -- !¡!Setting Values!¡!")

# Ensure the existence of the file and load its contents or create a new one
def load_or_create(file_path, default_content):
  if not os.path.exists(file_path):
    with open(file_path, 'w') as new_file:
      json.dump(default_content, new_file, indent=2)
      return default_content
  else:
    with open(file_path, 'r+') as file:
      try:
        return json.load(file)
      except:
        with open(file_path, 'w') as new_file:
          json.dump(default_content, new_file, indent=2)
          return default_content

# Define default values for each file
default_blocked_channels = []
default_members_count = {}
default_react_roles = {}
default_userdata = {}

# Load or create files with default content if they don't exist
blocked_channels = load_or_create("blocked_channels.json", default_blocked_channels)
members_count = load_or_create("MemberCount.json", default_members_count)
Settings.userdata = load_or_create("userdata.json", default_userdata)
react_roles = load_or_create("ReactRoles.json", default_react_roles)

print("[Python Bot] -- !¡!Values Set!¡!")
print("-------------------------------------")
