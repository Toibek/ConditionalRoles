import discord
from discord.ext import commands
from replit import db
import os
import datetime

client = discord.Client();
@client.event 
async def on_ready():
  print("Booted")

@client.event
async def on_message(message):
  msg = message.content
  if not msg.startswith('!') or message.author == client.user:
    return
  msg = msg[1::]
  print(message.flags)
  if "combo" in msg:
    split = msg.split(" ")
    if len(split) == 4: 
      roles = [
        split[1][3:-1:],
        split[2][3:-1:],
        split[3][3:-1:]
      ]
      for role in roles:
        print(role)
  roletoadd = message.author.guild.get_role(int(roles[2]))
  await message.author.add_roles(roletoadd)

  print(message.role_mentions)
  

  
client.run(os.environ['token'])

