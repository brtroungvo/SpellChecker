#import required dependities
import os
import discord
from discord.ext import commands
from autocorrect import Speller
from dotenv import load_dotenv

# Overrides system variables with .env variables
load_dotenv(override=True)

#
botToken = os.getenv("DISCORD_TOKEN")

#instantiate Speller object
text = Speller('en')

intents = discord.Intents.all()


#symbol to put before command
client = commands.Bot(command_prefix='?',intents=intents)


#shows online
@client.event
async def on_ready():   
    print("SpellChecker Status: Ready")
    print("-------------------------------------")


#gives commands and how to use them
@client.command()
async def hello(ctx):
    await ctx.send("```\nHello, I am SpellChecker\nMy command is spellcheck\nFormat for spellcheck is:\n?spellcheck \"<TEXT GOES HERE>\"\n```")



#given text, it will check the spelling
@client.command()
async def spellcheck(ctx, arg = "Missing argument"):
    await ctx.send("```\n"+text(arg)+"\n```")


#token goes in parentheses - dont give away very important
client.run(botToken)

# to add to server https://discord.com/api/oauth2/authorize?client_id=1149893802274869330&permissions=8&scope=bot

