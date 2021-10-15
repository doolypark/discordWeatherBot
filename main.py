import os
import discord
from discord.ext import commands

# creates discord client and stores it in "client"
# this is our bot
client = discord.Client()

@client.event
async def on_ready():
  print('Powering up {0.user}... ONLINE'.format(client))


# do stuff..
# bot function goes here
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!weather'):
    await message.channel.send('Complete your query...')



# Running client on the server
# the thing inside the parenthesis will be the Bot's token which is in discord dev website
# https://discord.com/developers/docs/intro
client.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg._mzQ5zFfxbuflFB06Em0E_b5sqM')


