from __future__ import unicode_literals
import discord
import asyncio
import praw
import random
import sys
import pprint
import urllib
import locale
#from pybooru import Danbooru
from discord.ext.commands import Bot
from discord.ext import commands

locale.setlocale(locale.LC_ALL,'')
Client = discord.Client()
bot_prefix="!"
client = commands.Bot(command_prefix=bot_prefix)

#Changes Tohru bot's Playing status.
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Ask for !help'))

#Tohru sends a random image once per day
async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        messages = ["https://thicc.moe/Bb7u8xYY9uKOBPtoPgCpPKcgamt7N8ys.jpg", "https://thicc.moe/hEPEZQ9ufQOIQgkRjueKyQSRBUsgiluQ.jpg", "https://thicc.moe/lplnLJiw2G3UqdUnmwID99kvEL2Ntry1.jpg", "https://thicc.moe/8PWWL0fPGHaqMk0enffu00JDyQzAY5Xo.jpg", "https://thicc.moe/Hbd0TTrXb6fwIdZFnluMsQMnNpn81r1X.png", "https://thicc.moe/6GiUPeb6QYnN1c8gWHzMNwCj7VlEeXJp.png", "https://thicc.moe/DKL1xPgfD16HkcxIkFMLVcusv1k2KaP8.jpg"]
        await client.send_message(channel, random.choice(messages))
        await asyncio.sleep(1440)

#Tohru replies. Main source of interaction!
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    message.content = message.content.lower() 
    if message.author == client.user:
        return

#Tohru says hi!
    if message.content.startswith('!hello'):
        msg = 'What do you want, {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

#Tohru says hi!
    if message.content.startswith('!hi'):
        msg = 'Do not speak to me so casually, {0.author.mention}!'.format(message)
        await client.send_message(message.channel, msg)

#Tohru says bye :(
    if message.content.startswith('!bye'):
    	msg = 'Hmph! Don\'t show yourself to me again, {0.author.mention}!'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru says 39!
    if message.content.startswith('!thanks'):
    	msg = 'https://imgur.com/26IDOGP'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru becomes strong.
    if message.content.startswith('!strong'):
    	msg = 'https://imgur.com/zc3sQBo'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru's eating!
    if message.content.startswith('!eat'):
    	msg = ['https://i.imgur.com/l3vqO0b.gif', 'https://imgur.com/7zfQasF']
    	await client.send_message(message.channel, random.choice(msg))

#Tohru's excited!
    if message.content.startswith('!genki'):
    	msg = 'https://imgur.com/GJX1kpg'.format(message)
    	await client.send_message(message.channel, msg)
		
#Tohru's tail!
    if message.content.startswith('!tail'):
    	msg = 'https://imgur.com/WD8fqcV'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru shows her... (´・ω・｀)
    if message.content.startswith('!butt'):
    	msg = 'https://imgur.com/dYDtFUr'.format(message)
    	await client.send_message(message.channel, msg)
		
#Tohru is happy!
    if message.content.startswith('!happy'):
    	msg = 'https://imgur.com/Hr8i6GC'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru has an idea
    if message.content.startswith('!idea'):
    	msg = ['https://imgur.com/WAkhTto', 'https://imgur.com/oiqs9nw']
    	await client.send_message(message.channel, random.choice(msg))

#Tohru is smug.
    if message.content.startswith('!smug'):
    	msg = ['https://imgur.com/sL0ybL0', 'https://imgur.com/A8io49g']
    	await client.send_message(message.channel, random.choice(msg))

#Tohru shrugs.
    if message.content.startswith('!shrug'):
    	msg = 'https://imgur.com/sL0ybL0'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru breathes fire!
    if message.content.startswith('!fire'):
    	msg = 'https://imgur.com/bCmNUcy'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru is confused!
    if message.content.startswith('!confused'):
    	msg = 'https://imgur.com/aB449DM'.format(message)
    	await client.send_message(message.channel, msg)
		
#Tohru is mad!
    if message.content.startswith('!mad'):
    	msg = 'https://imgur.com/MZQbjYs'.format(message)
    	await client.send_message(message.channel, msg)
		
#Tohru is sad :(
    if message.content.startswith('!sad'):
    	msg = 'https://imgur.com/UftCp38'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru pouts
    if message.content.startswith('!pout'):
    	msg = 'https://imgur.com/YohNnyI'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru cleans!
    if message.content.startswith('!clean'):
    	msg = 'https://imgur.com/jGyeDDX'.format(message)
    	await client.send_message(message.channel, msg)
		
#Tohru fights
    if message.content.startswith('!fight'):
    	msg = 'https://sakugabooru.com/data/4e69d088fa5a0410a5dfaaf42e656679.webm'.format(message)
    	await client.send_message(message.channel, msg)

#Tohru posts Kanna!
    if message.content.startswith('!kanna'):
    	msg = ['https://imgur.com/J6StUMs', 'https://imgur.com/tn1puZd', 'https://imgur.com/TcgTieH', 'https://imgur.com/LICIZIm']
    	await client.send_message(message.channel, random.choice(msg))	

#Tohru sends a list of help commands!
    if message.content.startswith('!help'):
	    msg = 'Hello {0.author.mention}! Here are a list of commands that Tohru recognizes! ```Markdown\n# - Here are the list of commands Tohru recognizes: - # \n\n!hello, !hi - Tohru says hi! \n!genki - Returns Tohru\'s energy level. \n!confused - Tohru is confused. \n!butt - Tohru shows her butt...? \n!eat - Tohru eats! \n!fire - Tohru breathes fire! \n!smug - Tohru becomes smug. \n!happy - Returns a happy Tohru. \n!idea - Tohru has an idea! \n!strong - Returns a strong Tohru. \n!mad - Returns a mad Tohru. \n!sad - Returns a sad Tohru. \n!clean - Tohru cleans! \n!pout - Tohru pouts. \n!kanna - Tohru posts Kanna! \n!tail - Tohru shows you her tail. \n!shrug - Returns an apathetic Tohru. \n\n# - Shitposting - # \n\n!pic - In progress!  ```'.format(message)
	    await client.send_message(message.channel, '{0.author.mention} I\'ve sent you a list of commands, you dirty human.'.format(message))
	    await client.send_message(message.author, msg)

#Tohru gets poked and replies!
    if message.content.startswith('!poke'):
    	msg = ['Stop!', 'I\'ll kill you!', 'You better stop now, or else...!', 'Who said you could touch me!', 'Keep your hands to yourself, you dirty mongrel!']
    	await client.send_message(message.channel, random.choice(msg))
		
#Tohru replies with eating gifs!
    if "pizza" in message.content:
    	msg = ['https://imgur.com/RZqBCRv', 'https://imgur.com/7zfQasF', 'https://imgur.com/l3vqO0b', 'https://imgur.com/n6gTPJe', 'https://imgur.com/THDlMcH', 'https://imgur.com/j9SLCCa']
    	await client.send_message(message.channel, random.choice(msg))
		
    if "hungry" in message.content:
    	msg = ['https://imgur.com/RZqBCRv', 'https://imgur.com/7zfQasF', 'https://imgur.com/l3vqO0b', 'https://imgur.com/n6gTPJe', 'https://imgur.com/THDlMcH', 'https://imgur.com/j9SLCCa']
    	await client.send_message(message.channel, random.choice(msg))
	
    if "food" in message.content:
    	msg = ['https://imgur.com/RZqBCRv', 'https://imgur.com/7zfQasF', 'https://imgur.com/l3vqO0b', 'https://imgur.com/n6gTPJe', 'https://imgur.com/THDlMcH', 'https://imgur.com/j9SLCCa']
    	await client.send_message(message.channel, random.choice(msg))
	
client.loop.create_task(background_loop())	
client.run("")
