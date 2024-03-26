import os
import random
from Configs.basic_utils import greeting_responses

import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "hello", description = "Greets the user!", aliases = ["hi", "hey"])
    async def hello(self, ctx: commands.Context) -> None:

        await ctx.reply(f"{ctx.author.mention}\n{random.choice(greeting_responses)}", ephemeral = True)

    @commands.hybrid_command(name = "logs", description = "Displays the events.log file!")
    async def logs(self, ctx: commands.Context) -> None:

        await ctx.send("Here's the `events.log` file you requested for!",
                       file = discord.File("Database/events.log"))

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Basic(client))