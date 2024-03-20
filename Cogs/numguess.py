import random
import asyncio
import logging

from discord import app_commands
from discord.ext import commands

class NumGuess(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "numguess", description = "Start a Number Guessing Game!")
    @app_commands.describe(max_limit = "What should be the maximum number limit for this game?")
    @commands.guild_only()
    async def numguess(self, ctx: commands.Context, max_limit: int) -> None:

        if max_limit >= 1000:
            await ctx.reply("Maximum number limit cannot be more than 1000!")
            return
        
        if max_limit <= 10:
            await ctx.reply("Maximum number limit cannot be less than 10!")
            return

        await ctx.reply(f"Okay! The maximum limit has been set to `{max_limit}` for this game!\n"
                        "Start giving your number guesses now!\n"
                        "You only get 5 tries though!")
        
        answer = random.randint(1, max_limit)
        
        for x in range(5):
            
            try:
                guess = await self.client.wait_for("message",
                                                timeout = 60,
                                                check = lambda m: (m.channel == ctx.channel
                                                                    and m.author == ctx.author
                                                                    and m.content.isdigit() is True))
                
            except asyncio.TimeoutError:
                await ctx.reply("Why did you start the game if you didn't wanna play ;-;")
                return
            
            else:
                
                if int(guess.content) < answer:
                    await guess.reply("Higher!")

                elif int(guess.content) > answer:
                    await guess.reply("Lower!")

                else:
                    await guess.reply("You got it!\n"
                                      f"The correct number was indeed **{answer}**\n"
                                      f"It took you {x + 1} tries to guess the correct number!")
                    return
                
        await ctx.reply("Game Over!\n"
                        f"The correct number was **{answer}**\n"
                        "Better luck next time!")
        
    @numguess.error
    async def numguess_error(self, ctx: commands.Context, error: commands.CommandError) -> None:

        if isinstance(error, commands.MissingRequiredArgument):
            logging.error(error)
            await ctx.reply("You're missing a required input for running this command!")

        elif isinstance(error, commands.BadArgument):
            logging.error(error)
            await ctx.reply("You didn't specify the inputs properly. Please check your command and try again!")

        else:
            logging.error(error)
            await ctx.send(":(\n\nAn unknown error occurred during the command execution.\n"
                        "To know further about the error info.. use the `>logs` command to fetch the `events.log` "
                        "file from the database!")
        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(NumGuess(client))

