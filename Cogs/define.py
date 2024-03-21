import discord
import os
import datetime

import requests
from discord.ext import commands
from discord import Embed

class Define(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.hybrid_command(name = "define", description = "query through the urban dictionary!")
    @commands.guild_only()
    async def define(self, ctx: commands.Context, *, word: str):
        url = f"https://api.urbandictionary.com/v0/define?term={word}"

        response = requests.get(url)
        data = response.json()

        if data["list"]:
            definition = data["list"][0]["definition"]
            example = data["list"][0]["example"]
            
            ud_embed = Embed(

                title = "URBAN DICTIONARY DEFINITIONS",
                description = f"**{word.capitalize()}**: {definition}\n\n*Example*: {example}",
                color = discord.Color.random(),
                timestamp = datetime.datetime.now()       
            )
            ud_embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar.url)
            await ctx.send(embed = ud_embed)
            
async def setup(client: commands.Bot):
    await client.add_cog(Define(client))