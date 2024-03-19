from utils import load_afk, save_afk

import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:

        afk_data = load_afk()

        if message.author == self.client.user:
            return
        
        elif afk_data[message.author.id] is not None:
            await message.channel.send(f"Welcome back {message.author.mention}!\n"
                                       f"You had gone AFK <t:{afk_data[message.author.id]["timestamp"]}:R>\n"
                                       f"Reason: **{afk_data[message.author.id]["reason"]}**")
        else:
            for user in message.mentions:
                
                if afk_data[user.id] is not None:
                    await message.reply(f"{user.mention} went AFK <t:{afk_data[user.id]["timestamp"]}:R>\n"
                                        f"Reason: **{afk_data[user.id]["reason"]}**")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Messages(client))