# Import Local files
import Settings


# Import the bot constructor
bot = Settings.Constructor.bot

print("[Python Bot] -- !¡!On Message event loading!¡!")

def event():
  def decorator(func):
    command_name = func.__name__  # Get the function name as the command name
    Settings.Functions.OnMessage[command_name] = func
    return func
  return decorator

@bot.event
async def on_message(ctx):
  for command_name in Settings.Functions.OnMessage:
    func = Settings.Functions.OnMessage[command_name]
    await func(ctx)
