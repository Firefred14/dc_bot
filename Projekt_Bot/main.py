import discord
from discord import message
from discord.ext import commands
import webbrowser
import os

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='$', intents=intents, case_insensitive=True)

#import all of the cogs
#from text_cog import text_cog 
#from music_cog import music_cog
#from reaction_cog import reaction_cog

# bot prefix
bot = commands.Bot(command_prefix='$')
bot.remove_command('help')

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

#register the class with the bot
#bot.add_cog(text_cog(bot))
#bot.add_cog(reaction_cog(bot))
#bot.add_cog(music_cog(bot))

#start the bot with my token
token = ""
with open ("token.txt") as file:
    token = file.read()
bot.run(token)






