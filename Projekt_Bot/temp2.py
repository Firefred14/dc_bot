import discord
import webbrowser
import os

welcome_channel_id = 829317380605870120
class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt. Beep bop.")
        welcome_channel = bot.get_channel(welcome_channel_id)
        await welcome_channel.send("Hallo auf Danis Discord Server. Bitte reagiere mit 🎮 für die Gaming Rolle und/oder mit 🎓 für die Uni Rolle.")


    async def on_reaction_add(self, reaction, user):
        zocken = discord.utils.get(user.guild.roles, name="Zocken")
        uni = discord.utils.get(user.guild.roles, name="Uni")
        if str(reaction.emoji) == "🎮":
            await user.add_roles(zocken)
        if str(reaction.emoji) == "🎓":
            await user.add_roles(uni)



bot = MyClient()
bot.run("ODI5NDI2NDMxOTIyMjc0MzM0.YG39jw.xVAuvDm2vzNoBE7_I7A0tfkrwyQ")