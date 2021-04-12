import discord
from discord.ext import commands
import os

#from dotenv import load_dotenv
#load_dotenv()

#dont use requests use aiohttp for Async like discord
#import json

#client = discord.Client()
client = commands.Bot(command_prefix="!")

cmdList=    '''COMMANDS: \n
            !nifty [WC name]: returns design from Nifty Senpai \n
            !lizard : DMs 'wizard' \n
            !website : returns a website link \n
            !help : returns command list \n
            !commands : returns commands list \n
            Also some song lyrics will be responded to, everything moves, i think it might be fear, ashfur etc.'''
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f"Welcome {member}!")

@client.event
async def on_member_remove(member):
    print(f"Au Revoir, {member}.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Everything moves'):
        await message.channel.send(content='everything pulses')
    if message.content.startswith('I think it might be fear'):
        await message.channel.send(content='Of the world and the way it makes you feel afraid')
    if message.content.startswith('They tried to put me on the cover of vogue'):
        await message.channel.send(content='But my legs were TOOOO LOOOONGGG')
    if message.content.startswith('Every day is leg day') or message.content.startswith('Everyday is leg day'):
        await message.channel.send(content='Monday Tuesday Wednesday, Thighs Calves all the way')
    if message.content.startswith('Ashfur'):
        await message.channel.send(content='God you are four of the ugliest fucking kids I have ever had the misfortune of laying my eyes on. I can\'t wait for this bitch to kill you')

    if message.content.startswith('!website'):
        await message.author.send(content='https://niftysenpai.carrd.co/')

#https://warriorsproject.tumblr.com/post/614347760127393792/im-big-dumbdumb-and-didnt-keep-the-og-post-so-i
#https://warriorsproject.tumblr.com/tagged/firestar
#https://github.com/JGrahamH/Jarvis-Discord-Bot

@client.command()
async def memeHouses(ctx):
    await ctx.send('https://discord.gg/MFmnJ6c')
    print("command worked cmd=discord")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")
    print("command worked cmd=Hello")

@client.command()
async def logout(ctx):
    await client.logout()

@client.command()
async def lizard(ctx):
    await ctx.author.send('wizard')
    print("command worked cmd=lizard")

@client.command()
async def rost(ctx):
    await ctx.send("You are a squid")
    print("command worked cmd=rost")

@client.command()
async def help(ctx):
    await ctx.send(cmdList)
    print("command worked cmd=Help")


client.run('ODMwMTY3MDgxMTQyOTc2NTcy.YHCvVw.bxrYLFzYwRY6TpEydYE1MKbayX4')
#client.run(os.getenv('TOKEN'))