#DISCORD
import discord
from discord.ext import commands

#OTHER-IMPORTS
import json
import time
import random
import datetime

config = json.load(open('config.json'))

client = commands.Bot(command_prefix=config["prefix"], description="A very nice general bot for memes, music and moderation and also for other stuffs, coded in python3.7 with ❤ by Cyraxx#7959", pm_help=True, owner_id=510096668633464843, case_insensitive=True, activity=discord.Game(name="Starting the bot...."), status=discord.Status("dnd"))

client.remove_command("help")

#from red-discordbot
client._uptime = None

@client.event

async def on_connect():
	if client._uptime is None:
		print(f"Connected to Discord. Getting ready...")
		print(f'-----------------------------')
	
#on_ready
@client.event
async def on_ready():
	client.starttime = time.time()
	print(f'--------------------------------')	
	print(f'Bot ready!')
	print(f"Succesfully logged in as: {client.user.name}")	
	print(f"ID: {client.user.id}")
	print(f"Total servers: {len(client.guilds)}")	
	print(f"Total Members: {len(client.users)}")	
	print(f"Discord.py version: {discord.__version__}")
	print(f'--------------------------------')
	#Change Name to your name
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="CyraxxOP"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.author == message.author.bot:
            return

    await client.process_commands(message)
            
    if re.match(f"^<@!?{client.user.id}>$", message.content):
        msg = f"""
        **My Prefix here is**   `{botprefix}`
        """
        return await message.channel.send(msg)


@client.command(usage="A simple hi command", aliases=["aliases", "example"])
async def hi(ctx):    

    await ctx.send("Hi there 😄")

@client.command(usage= "Adds two numbers")
async def add(ctx, a: int, b: int): 
    await ctx.send(a + b)   

@client.command(usage= "Subtracts two numbers")
async def minus(ctx, a: int, b: int):
    await ctx.send(a - b)    

@client.command(usage="Multiplies two numbers")
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)  

@client.command(usage= "Divides two numbers")
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)
    
#embed example
@client.command(usage='Abey Sale, meme', aliases=['abesale', 'absale', 'abbesale'])
async def abeysale(ctx):
        em=discord.Embed(colour=0x7289DA)    
        em.set_author(name="Abe Sale 😐", icon_url=ctx.me.avatar_url)
        em.set_image(url="https://media.tenor.com/images/957138de6ff6e239f433a7818dca77f3/tenor.gif")
        em.set_footer(text=f"A very nice meme", icon_url=ctx.author.avatar_url)        
        try:
            await ctx.send(embed=em)
        except:
            await ctx.send("An error occured please report it to the support server sorry :no_entry:")
                       
##on_guild_join   Example##        
@client.event
async def on_guild_join(guild):
   owner= client.get_user(guild.owner.id)
   colors = [0xff0000, 000000]
   em = discord.Embed(color = random.choice(colors))
   em.set_author(name=f"Hello, Thankyou for Inviting me!", icon_url = client.user.avatar_url)
   em.add_field(name=f"CyraxxBoT", value=f"""**Hey! CyraxxBoT is here. I am ready to revive  your server: __{guild.name}__ with an id of: __{guild.id}__.
Server has:- 
__{len(guild.channels)} channels__
__{len(guild.roles)} roles__**""", inline=False)
   em.add_field(name=f"Prefix:", value=f"My Prefix is `{config['prefix']}`", inline=False)
   em.add_field(name=f"About Me", value=f"""**I am a Multipurpose discord-bot for your needs which includes __Music, Moderation, Fun, Memes, Utility and also for other stuffs__, coded by `YourName` or Cyraxx.
My support server: (https://discord.gg/HKtQmtj)**""", inline=False)
   try:
      await owner.send(embed=em)
   except Exception as e:
      print(e)
      pass

##A very nice embed simple help command example
@client.command()
async def help(ctx):
    help= "**"
    for command in client.commands:
        help+=f"{command}- `{command.usage}`\n"
    help+="**"   
    embed=discord.Embed(color=0x0000, title="My Commands", description=help)
    embed.set_footer(text="Created by Cyraxx") #Change
    embed.set_thumbnail(url='https://image.ibb.co/caM2BK/help.gif')
    embed.set_image(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')

    await ctx.send(embed=embed)

#RUNNING OUR BOT            
client.run(config["token"])
