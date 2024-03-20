import random
from utils import load_afk, save_afk, snapcap_responses

import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:

        afk_data = load_afk()
        chances = [0,1]
        weights = [0.6, 0.4]
        will_respond = random.choices(chances, weights=weights)

        if message.author == self.client.user:
            return
        
        elif message.content.startswith(">afk"):
            return
        
        elif afk_data.get(str(str(message.author.id))) is not None:
            await message.channel.send(f"Welcome back {message.author.mention}!\n"
                                       f"You had gone AFK <t:{afk_data[str(message.author.id)]["timestamp"]}:R>\n"
                                       f"Reason: **{afk_data[str(message.author.id)]["reason"]}**")
            
            del afk_data[str(message.author.id)]
            save_afk(afk_data)
            return
            
        for user in message.mentions:
            
            if afk_data.get(str(str(user.id))) is not None:
                await message.reply(f"{user.mention} went AFK <t:{afk_data[str(user.id)]["timestamp"]}:R>\n"
                                    f"Reason: **{afk_data[str(user.id)]["reason"]}**")
                
        if message.content.lower().find("snapcap") != -1 or message.content.lower().find("snap") != -1:
            
            if will_respond[0] == 0:
                await message.reply(random.choice(snapcap_responses))

        elif message.content.lower().find("home") != -1:
            
            if will_respond[0] == 0:
                await message.reply("Did you mean hoe-m?")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Messages(client))