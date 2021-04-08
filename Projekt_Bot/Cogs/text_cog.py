import discord
from discord.ext import commands


class text_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
ich höre auf folgende Kommandos:
$help - Ich zeige dir alle Befehle an.
$clear <Anzahl> - Löscht die letzten X Nachrichten.
$ts - Ich zeige dir die Zugangsdaten zum Teamspeak Server.

Music commands:
$play <Suchbegriff> - Durchsucht Youtube nach deinem Wunschsong.
$queue - Zeigt dir die nächsten Lieder an.
$skip - Skippt ein lied weiter.
```
"""
        self.text_channel_list = []

    #some debug info so that we know the bot has started    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_list.append(channel)

        #await self.send_to_all(self.help_message)        

    @commands.command(name="help", help="Zeigt den Hilfetext an.")
    async def help(self, ctx):
        await ctx.send(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)

    @commands.command(name="clear", help="löscht die letzten x Nachrichten.")
    async def clear(self, ctx, arg):
        #extract the amount to clear
        amount = 5
        try:
            amount = int(arg)
        except Exception: pass

        await ctx.channel.purge(limit=amount)

    @commands.command(name="hallo", help="Welcome Greetings from the Bot.")
    async def hello(self, ctx):
        await ctx.send("""
```
Hallo, ich höre auf folgende Kommandos:
$help - Ich zeige dir alle Befehle an.
$clear <Anzahl> - Löscht die letzten X Nachrichten.
$ts - Ich zeige dir die Zugangsdaten zum Teamspeak Server.

Music commands:
$play <Suchbegriff> - Durchsucht Youtube nach deinem Wunschsong.
$queue - Zeigt dir die nächten Lieder an.
$skip - Skippt ein lied weiter.
```
""")

    @commands.command(name="Ts", help="Welcome Greetings from the Bot.")
    async def ts(self, ctx):
        await ctx.send("Die Zugangsdaten zum TS Server sind: 62.104.20.82:10062 \nFalls du keine Rechte haben solltest um in den richtigen Channel zu gelangen, wende dich bitte an einen Admin.")


def setup(client):
    client.add_cog(text_cog(client))
    print('text cog is loaded')