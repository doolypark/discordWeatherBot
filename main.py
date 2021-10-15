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
bot.run('ODk3MjQxNzgxODM2NTgyOTIz.YWSzhg.oCVn7AsAmXS6Vl02vphLDVim8v0')
