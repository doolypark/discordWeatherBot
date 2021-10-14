import os
import discord
from discord.ext import commands

# creates discord client and stores it in "client"
# this is our bot
client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')




# do stuff..
# bot function goes here



# Running client on the server
# the thing inside the parenthesis will be the Bot's token which is in discord dev website
# https://discord.com/developers/docs/intro
client.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg.Uibrdx3tX5yURDM6MK_jjVYdBIQ')


