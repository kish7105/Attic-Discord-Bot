import time
from utils import load_afk, save_afk

from discord.ext import commands

class AFK(commands.Cog):

    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    @commands.hybrid_command(name = "afk", description = "Sets your status to AFK!")
    @commands.guild_only()
    async def afk(self, ctx: commands.Context, *, reason: str = "Not Provided") -> None:
        
        afk_data = load_afk()

        if afk_data[ctx.author.id] is not None:
            await ctx.reply(f"Welcome back {ctx.author.mention}!")  # not completed yet

            del afk_data[ctx.author.id]
            save_afk(afk_data)

        else:
            afk_data[ctx.author.id] = {
                "timestamp": time.time(),
                "reason": reason
            }
            save_afk(afk_data)
            
            # time.time() represents an 'unix' timestamp
            await ctx.send(f"{ctx.author.name} went AFK <t:{time.time()}:R>\nReason: **{reason}**")

async def setup(client: commands.Bot) -> None:
    await client.add_cog(AFK(client))