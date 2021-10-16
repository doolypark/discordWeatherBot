import os
import discord
from discord.ext import commands

# creates discord client and stores it in "client"
# this is our bot
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Powering up {0.user}... ONLINE'.format(bot))


@bot.event
async def on_disconnect():
    print("Robot dying noise...")


# do stuff..
# bot function goes here
@bot.command()
async def weather(ctx):
    await ctx.reply("Make sure you type your location.\n *Example: !weather Dallas, Texas, USA*")

# Running client on the server
# the thing inside the parenthesis will be the Bot's token which is in discord dev website
# https://discord.com/developers/docs/intro
bot.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg.ZcBZZQeIADmMNiXXQBhm5gcCxnU')
'''
prefix = "!weather"
client = commands.Bot(command_prefix=prefix)


@client.event
async def on_ready():
    print('Powering up {0.user}... ONLINE'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the sky for you"))


@client.event
async def on_message(message):
    # checks if the person who sent the message is NOT the bot and it starts with the prefix
    if message.author != client.user and message.content.startswith(prefix):
        await message.channel.send(message.content)
        await message.channel.send(type(message.content))


client.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg.ZcBZZQeIADmMNiXXQBhm5gcCxnU')
