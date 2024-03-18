import random

import discord
from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        pass

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Messages(client))