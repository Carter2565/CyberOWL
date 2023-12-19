import Settings

commands = [
  ':regional_indicator_c: :regional_indicator_o: :regional_indicator_m: :regional_indicator_m: :regional_indicator_a: :regional_indicator_n: :regional_indicator_d: :regional_indicator_s: :',
  f'''**{Settings.operator}h/{Settings.operator}help **
  The help command displays this list 
  
  Use this key for understanding the commands:
  `<Required argument>` `[Optional argument]`
    
  **{Settings.operator}hi/{Settings.operator}hello **
  A friendly hello
  ''',
# End of pg.1	
  f'''# Common commands:
  ## **{Settings.operator}get_reactions <Channel_ID> <Message_ID> **
  Parameters separated by a space.
  Channel_ID => DM Channel ID/ Server Channel ID
  Message_ID => DM Message ID/ Server Message ID

  This command displays the reactions on a message!
  
  ## **{Settings.operator}block_channel <Channel_ID> **
  Channel_ID => DM Channel ID/ Server Channel ID

  This command disables/enables bot commands from this bot on a specific channel!
  ''',
# End of pg.2	
  f'''# Server only commands:
  ## **{Settings.operator}member_count/{Settings.operator}members [Config] **
  ### Config => config, members, online, offline, update
  **config**: This brings the default config prompts.
  **members**: This enables the ability to modify/create the **Member Count** channel.
  **online**: This enables the ability to modify/create the **Online Count** channel.
  **offline**: This enables the ability to modify/create the **Offline Count** channel.
  **update**: This updates the counts.
  ''',
# End of pg.4
  f'''End of document
  ''',
]


 