import discord
from discord.ext import commands
import webbrowser
import os



channel_id = 764819318885056552

#import all of the cogs
from main_cog import main_cog
from image_cog import image_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(main_cog(bot))
bot.add_cog(image_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run(os.getenv("TOKEN"))



class MyClient(discord.Client): 
    #einloggen
    async def on_ready(self):
        print("bin on digga")

    #Wenn Nachricht gesendet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("Hallo Bot") and message.channel.id == channel_id:
            #if (message.channel.id == channel_id): 
                await message.channel.send("Hallo " + str(message.author) + ", \nwenn du wissen möchtest wer mein Vater ist gebe $Papi ein. :) \nWenn du wissen willst wie die Zugangsdaten zum Farmersfiver TS sind, gebe $Ts ein. ")

        if message.content == "$Papi" and message.channel.id == channel_id: 
            await message.channel.send("Mein Papi ist Dani.") 

        if message.content == "$Ts" and message.channel.id == channel_id:
            await message.channel.send("Die Zugangsdaten zum TS Server sind: 62.104.20.82:10062 \nFalls du keine Rechte haben solltest um in den richtigen Channel zu gelangen, wende dich bitte an einen Admin.")

token = ""
with open ("token.txt") as file:
    token = file.read()

client = MyClient()
#client = commands.Bot(command_prefix='/')
#client.add_cog(music_cog(client))


client.run(token)
#client.run(os.getenv(token))








