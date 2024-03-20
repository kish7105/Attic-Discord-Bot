import random 

import discord
from discord.ext import commands

responses = [
    "Hey there!",
    "Hi!",
    "Hello!",
    "Hey!",
    "Hi, how are you?",
    "Hello, good to see you!",
    "Hey, what's up?",
    "Hi, nice to meet you!",
    "Hello, how have you been?",
    "Hey, how's it going?",
    "Hi, how's your day?",
    "Hello, how are things?",
    "Hey, long time no see!",
    "Hi there, how can I help you?",
    "Hello, what's new?",
    "Hey, howdy!",
    "Hi, good to hear from you!",
    "Hello, nice weather today, isn't it?",
    "Hey, how's everything going?",
    "Hi, what's going on?"
]

class Basic(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "hello", description = "Greets the user!", aliases = ["hi", "hey"])
    async def hello(self, ctx: commands.Context) -> None:

        await ctx.reply(f"{ctx.author.mention}\n{random.choice(responses)}", ephemeral = True)

    @commands.hybrid_command(name = "logs", description = "Displays the events.log file!")
    async def logs(self, ctx: commands.Context) -> None:

        await ctx.send("Here's the `events.log` file you requested for!",
                       file = discord.File("Database/events.log"))

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Basic(client))