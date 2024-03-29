import asyncio
import logging
from Configs.rps_utils import SinglePlayerRPS, MultiPlayerAuthorRPS

import discord
from discord import app_commands
from discord.ext import commands


        
class RockPaperScissors(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "srps", description = "Start a singleplayer Rock, Paper & Scissors Game!")
    @commands.guild_only()
    async def srps(self, ctx: commands.Context) -> None:

        srps_view = SinglePlayerRPS(ctx)
        srps_view.message = await ctx.send(f"{ctx.author.mention}\nChoose Rock, Paper or Scissors!",
                                           view = srps_view)
        
    @commands.hybrid_command(name = "mrps", description = "Start a Multiplayer game of Rock, Paper & Scissors!")
    @app_commands.describe(user = "Who do you wanna play with?")
    @commands.guild_only()
    async def mrps(self, ctx: commands.Context, user: discord.Member) -> None:

        await ctx.send(f"{user.mention}!\n\n"
                       f"{ctx.author.mention} just challenged for a Rock, Paper & Scissors Game\n"
                       "To accept the challenge, enter ``accept`` in the chat or else type ``reject`` if you "
                       "ain't down for the challenge")

        try:
            user_response = await self.client.wait_for("message", timeout = 120,
                                                   check = lambda m: (m.channel == ctx.channel 
                                                                      and m.author.id == user.id
                                                                      and m.content.lower() in ["accept", "reject"]))
        except asyncio.TimeoutError:
            await ctx.reply(f"{user.name} didn't respond.\nSadge :(")
            return
        
        else:
            if user_response.content == "reject":
                await ctx.reply(f"{user.mention} didn't accept your challenge. lol")
                return
            
            mrps_view = MultiPlayerAuthorRPS(ctx, user)
            mrps_view.message = await ctx.send(f"{ctx.author.mention}\nChoose Rock, Paper or Scissors!",
                                               view = mrps_view)
            
    @srps.error
    async def srps_error(self, ctx: commands.Context, error: commands.CommandError):
        
        logging.error(error)
        await ctx.send(":(\n\nAn unknown error occurred during the command execution.\n"
                       "To know further about the error info.. use the `>logs` command to fetch the `events.log` "
                       "file from the database!")

    @mrps.error
    async def srps_error(self, ctx: commands.Context, error: commands.CommandError):

        if isinstance(error, commands.MissingRequiredArgument):
            logging.error(error)
            await ctx.reply("Please mention an user you want to play with!")

        elif isinstance(error, commands.BadArgument):
            logging.error(error)
            await ctx.reply("Oops.. An error occurred.\nPlease check if your inputs are valid!")

        else:
            logging.error(error)
            await ctx.send(":(\n\nAn unknown error occurred during the command execution.\n"
                           "To know further about the error info.. use the `>logs` command to fetch the `events.log` "
                           "file from the database!")
    
async def setup(client: commands.Bot) -> None:
    await client.add_cog(RockPaperScissors(client))