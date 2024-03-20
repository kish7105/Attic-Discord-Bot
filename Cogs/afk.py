import time
import datetime
from utils import load_afk, save_afk

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
        
        afk_data = load_afk()

        if afk_data.get(str(ctx.author.id)) is not None:
            await ctx.reply(f"Welcome back {ctx.author.mention}!\n"
                            f"You had gone AFK <t:{afk_data[str(ctx.author.id)]["timestamp"]}:R>\n"
                            f"Reason: **{reason}**")

            del afk_data[str(ctx.author.id)]
            save_afk(afk_data)

        else:
            afk_data[str(ctx.author.id)] = {
                "timestamp": int(time.time()),
                "reason": reason
            }
            save_afk(afk_data)

            embed = discord.Embed(
                description = f"{ctx.author.name} went AFK <t:{int(time.time())}:R>",
                color = discord.Color.random(),
                timestamp = datetime.datetime.now()
            )

            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar.url)
            embed.add_field(name = "Reason:", value = f"```{reason}```", inline = False)
            
            # time.time() represents an 'unix' timestamp
            await ctx.send(embed = embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(AFK(client))