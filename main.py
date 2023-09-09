#import required dependities
import discord
from discord.ext import commands
from autocorrect import Speller

#import Bot Token
from tokens import *

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
    try:
        await ctx.send("```\nHello, I am SpellChecker. My prefix is ? and my commands are help and spellcheck.\nFormat for spellcheck is:\n?spellcheck \" \"\n```")
    except:
        print("An exception occured")


#given text, it will check the spelling
@client.command()
async def spellcheck(ctx, arg = "Missing argument"):
    await ctx.send("```\n"+text(arg)+"\n```")


#token goes in parentheses - dont give away very important
client.run(botToken)

# to add to server https://discord.com/api/oauth2/authorize?client_id=1149893802274869330&permissions=8&scope=bot

