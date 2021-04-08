async def on_raw_reaction_add(payload):
        message_id = payload.message_id
        if message_id == 829328084415152138:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, bot.guilds)

            if payload.emoji.name == ':mortar_board:':
                role = discord.utils.get(guild.roles, name ='Uni')
            elif payload.emoji.name == ':video_game:':
                role = discord.utils.get(guild.role, name='Zocken')
                

            if role is not None:
                member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print("done")
                else: 
                    print("Member not found")
            else: 
                print("Role not found")            
                