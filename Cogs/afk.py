import time
import logging
from Configs.json_utils import load_afk, save_afk
from Configs.afk_utils import generate_afk_embed

import discord
from discord import app_commands
from discord.ext import commands

class AFK(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "afk", description = "Sets your status to AFK!")
    @app_commands.describe(reason = "Why are you going AFK? ( This parameter is optional )")
    @commands.guild_only()
    async def afk(self, ctx: commands.Context, *, reason: str = "Not Provided") -> None:
        
        afk_data = load_afk()  # load data from 'afk.json'

        if afk_data.get(str(ctx.author.id)) is not None:  # if the author is already afk
            await ctx.reply(f"Welcome back {ctx.author.mention}!\n"
                            f"You had gone AFK <t:{afk_data[str(ctx.author.id)]["timestamp"]}:R>\n"
                            f"Reason: **{reason}**")

            del afk_data[str(ctx.author.id)]  # erase author's data from 'afk.json'
            save_afk(afk_data)  # save the changes
            return
        
        # if the user isn't AFK, execute the code below

        afk_data[str(ctx.author.id)] = {
            "timestamp": int(time.time()),  # unix timestamp
            "reason": reason  # reason provided by the author
        }
        save_afk(afk_data)  # save the changes

        await ctx.send(embed = generate_afk_embed(ctx, reason))

    # Error Handler

    @afk.error
    async def afk_error(self, ctx: commands.Context, error: commands.CommandError) -> None:

        logging.error(error)
        await ctx.send(":(\n\nAn unknown error occurred during the command execution.\n"
                       "To know further about the error info.. use the `>logs` command to fetch the `events.log` "
                       "file from the database!")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(AFK(client))