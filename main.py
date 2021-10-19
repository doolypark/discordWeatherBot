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
        msg = message.content.split()

        # checks if users accidentally put more characters than the prefix
        if msg[0] != "!weather":
            await message.channel.send("Unrecognized command")
            await message.channel.send(msg)
        else:
            # checks if there is only 1 string which is just the prefix
            if len(msg) == 1:
                await message.channel.send(":exclamation:Complete your command by typing \"!weather City,State\"")
                await message.channel.send(msg)
            elif len(msg) == 2:
                await message.channel.send("Try checking your query. Example: !weather Dallas, Texas")
                await message.channel.send(msg)
            # this is where user have entered correct input
            elif len(msg) == 3:
                await message.channel.send("Valid input")
                await message.channel.send(msg)
            else:
                await message.channel.send(":exclamation:Something went wrong")






# Running client on the server
# the thing inside the parenthesis will be the Bot's token which is in discord dev website
# https://discord.com/developers/docs/intro
client.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg.MvwNJDuOKXJ9Zrdx6kke-cTnvk0')
