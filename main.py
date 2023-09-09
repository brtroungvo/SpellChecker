#import required dependities
import discord
from discord.ext import commands

#import Bot Token
from tokens import *


intents = discord.Intents.all()


#symbol to put before command
client = commands.Bot(command_prefix='?',intents=intents)


#shows online
@client.event
async def on_ready():   
    print("SpellChecker Status: Ready")
    print("-------------------------------------")


#says hello
@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am SpellChecker. My prefix is ? and some of my commands are hello and spellCheck")


#given text, it will check the spelling
@client.command()
async def spellcheck(ctx, arg):
    await ctx.send(arg.checker)


#spell checks the paragraph and sends it back
def checker(self, text):
    self.result = 


#token goes in parentheses - dont give away very important
client.run(botToken)

# to add to server https://discord.com/api/oauth2/authorize?client_id=1147985792661213185&permissions=8&scope=bot

