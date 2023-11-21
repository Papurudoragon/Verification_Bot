import discord
from discord.ext import commands
import os

my_secret = os.environ['token']
# client = discord.Client(intents=discord.Intents.all())
client = commands.Bot(command_prefix='/', help_command=None, intents=discord.Intents.all())
conversation_id = None
channel = client.get_channel(<channel ID>)

# Set up Discord command to trigger the function, get response from api, and send the response
@client.event
async def on_ready():
  print(f'Logged in as {client.user}')


# if a user joins, post a message in the verification channel
@client.event
async def on_member_join(member, message):
  member = member.author.name
  await message.channel.send(f'Hello! {member}, please verify yourself by using ```/verify```!')

# if user is already in the server, they can verify in the #verification channel
@client.event
async def on_message(message):
  if message.content.startswith('/verify'):
    role = discord.utils.get(message.guild.roles, name="Members (Verified)")
    if role not in message.author.roles:
      await message.author.add_roles(role)
      await message.channel.send(f'{message.author.mention} has been verified!')
    else:
      await message.channel.send(f'{message.author.mention}, you have already been verified!')

# Run the bot
try:
  client.run(my_secret) #set intents in the discord app page to run this  
  # client.run(os.getenv('DISCORD_BOT_TOKEN')) ---------> not used with replit
  
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    os.system("python restarter.py")
    os.system('kill 1')
