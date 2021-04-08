import discord
from discord import message, ActivityType
from discord.ext import commands
from discord.ext.commands import Cog
from discord.utils import get

#intents = discord.Intents.all()
client = commands.Bot(command_prefix = '$', intents=intents)

class reaction_cog(commands.Cog):
    # Allows to access the client within the cog
    def __init__(self, client):
        self.client = client 

    @client.event
    #@commands.Cog.listener
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 829409323297407027:
            guild = client.get_guild(payload.guild_id)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)   
            if role != None:
                member = get(guild.members, id=payload.user_id)
                if member is not None:
                    await member.add_roles(role)          
                
    @client.event
    #@commands.Cog.listener
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 829409323297407027:
            guild = client.get_guild(payload.guild_id)
            role = discord.utils.get(guild.roles, name=payload.emoji.name)      
            if role != None:
                member = get(guild.members, id=payload.user_id)
                if member is not None:
                    await member.remove_roles(role)

def setup(client):
    client.add_cog(reaction_cog(client))
    print('reaction cog is loaded') 


#client.run("ODI5NDI2NDMxOTIyMjc0MzM0.YG39jw.xVAuvDm2vzNoBE7_I7A0tfkrwyQ")