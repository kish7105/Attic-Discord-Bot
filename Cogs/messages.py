import random
from Configs.json_utils import load_afk, save_afk
from Configs.basic_utils import snapcap_responses

import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:

        afk_data = load_afk()
        chances = [0,1]  # 0 if bot will reply, else 1
        weights = [0.6, 0.4]  # 60%( 0.6 ) chances that the bot will reply
        will_respond = random.choices(chances, weights=weights)[0]

        if message.author == self.client.user:  # if the bot itself is the author of the message
            return
        
        elif message.content.startswith(">afk"):  # if the author uses the afk command
            return
        
        elif afk_data.get(str(message.author.id)) is not None:  # if the message author was AFK
            await message.channel.send(f"Welcome back {message.author.mention}!\n"
                                       f"You had gone AFK <t:{afk_data[str(message.author.id)]["timestamp"]}:R>\n"
                                       f"Reason: **{afk_data[str(message.author.id)]["reason"]}**")
            
            del afk_data[str(message.author.id)]  # delete the author's data from 'afk.json'
            save_afk(afk_data)  # save the changes
            return
            
        for user in message.mentions:  # iterating over mentions in a message
            
            if afk_data.get(str(str(user.id))) is not None:  # if the user mentioned in the message is AFK
                await message.reply(f"{user.mention} went AFK <t:{afk_data[str(user.id)]["timestamp"]}:R>\n"
                                    f"Reason: **{afk_data[str(user.id)]["reason"]}**")
                
        if message.content.lower().find("snapcap") != -1 or message.content.lower().find("snap") != -1:
            
            if will_respond == 0:
                await message.reply(random.choice(snapcap_responses))

        elif message.content.lower().find("home") != -1:
            
            if will_respond == 0:
                await message.reply("Did you mean hoe-m?")

        elif message.content.lower().find("kish") != -1:
            
            if will_respond == 0:
                await message.reply("kish is my daddy🥵")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Messages(client))