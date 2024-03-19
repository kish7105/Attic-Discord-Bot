import asyncio
import random

import yaml
import discord
from discord.ui import View, button
from discord.ext import commands

def load_data():
    
    with open("Database/config.yml", "r") as file:
        return yaml.safe_load(file)
    
def save_data(data):

    with open("Database/config.yml", "w") as file:
        yaml.dump(data, file, default_flow_style = False)

def load_afk():
    
    with open("Database/afk.yml", "r") as file:
        return yaml.safe_load(file)

def save_afk(afk_data):

    with open("Database/afk.yml", "w") as file:
        yaml.dump(afk_data, file, default_flow_style = False)

snapcap_responses = [
    "Snap upni biwi ko divorce mat de",
    "Papa came back with the milk",
    "Papa mene blackie se shadi kar li",
    "Snap did you adopt again?",
    "Snap Manno ka pankha wapas karde",
    "I love you too",
    "We should sleep together"
]

class SinglePlayerRPS(View):

    def __init__(self, ctx: commands.Context) -> None:
        
        super().__init__(timeout = 120)
        self.ctx = ctx
        self.AI = random.choice(["Rock", "Paper", "Scissors"])

    async def on_timeout(self) -> None:

        for button in self.children:
            button.disabled = True
        
        await self.message.edit(view = self)
        await self.message.reply("The buttons have been disabled due to inactivity!")

    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Hey! Those options are not for you buddy", ephemeral = True)
            return False
        
        else:
            for button in self.children:
                button.disabled = True
        
            await self.message.edit(view = self)
            return True
        
    @button(label = "Rock", style = discord.ButtonStyle.green, emoji = "🪨")
    async def rock_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.AI == "Rock":
            await interaction.response.send_message("You chose: **Rock**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **IT'S A TIE!**")
            
        elif self.AI == "Paper":
            await interaction.response.send_message("You chose: **Rock**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU LOST!**")
            
        else:
            await interaction.response.send_message("You chose: **Rock**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU WON!**")
        
        self.stop()

    @button(label = "Paper", style = discord.ButtonStyle.green, emoji = "📰")
    async def paper_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.AI == "Rock":
            await interaction.response.send_message("You chose: **Paper**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU WON!**")
            
        elif self.AI == "Paper":
            await interaction.response.send_message("You chose: **Paper**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **IT'S A TIE!**")
            
        else:
            await interaction.response.send_message("You chose: **Paper**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU LOST!**")
        
        self.stop()

    @button(label = "Scissors", style = discord.ButtonStyle.green, emoji = "✂️")
    async def scissors_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.AI == "Rock":
            await interaction.response.send_message("You chose: **Scissors**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU LOST!**")
            
        elif self.AI == "Paper":
            await interaction.response.send_message("You chose: **Scissors**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **YOU WON!**")
            
        else:
            await interaction.response.send_message("You chose: **Scissors**\n"
                                                    f"AI chose: **{self.AI}**\n\n"
                                                    "Result: **IT'S A TIE!**")
        
        self.stop()

class MultiPlayerUserRPS(View):

    def __init__(self, ctx: commands.Context, user: discord.Member, author_choice: str) -> None:
        
        super().__init__(timeout = 120)
        self.ctx = ctx
        self.user = user
        self.author_choice = author_choice

    async def on_timeout(self) -> None:

        for button in self.children:
            button.disabled = True
        
        await self.message.edit(view = self)
        await self.message.reply("The buttons have been disabled due to inactivity!")

    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user != self.user:
            await interaction.response.send_message("Hey! Those options are not for you buddy", ephemeral = True)
            return False
        
        else:
            for button in self.children:
                button.disabled = True
        
            await self.message.edit(view = self)
            return True
        
    @button(label = "Rock", style = discord.ButtonStyle.green, emoji = "🪨")
    async def rock_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.author_choice == "Rock":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Rock**\n"
                                                    f"{self.user.mention} chose: **Rock**\n\n"
                                                    "Result: **IT'S A TIE!**")
            
        elif self.author_choice == "Paper":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Paper**\n"
                                                    f"{self.user.mention} chose: **Rock**\n\n"
                                                    f"Result: {self.ctx.author.mention} **WON!**")
            
        else:
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Scissors**\n"
                                                    f"{self.user.mention} chose: **Rock**\n\n"
                                                    f"Result: {self.user.mention} **WON!**")
            
        self.stop()

    @button(label = "Paper", style = discord.ButtonStyle.green, emoji = "📰")
    async def paper_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.author_choice == "Rock":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Rock**\n"
                                                    f"{self.user.mention} chose: **Paper**\n\n"
                                                    f"Result: {self.user.mention} **WON!**")
            
        elif self.author_choice == "Paper":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Paper**\n"
                                                    f"{self.user.mention} chose: **Paper**\n\n"
                                                    f"Result: **IT'S A TIE!**")
            
        else:
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Scissors**\n"
                                                    f"{self.user.mention} chose: **Paper**\n\n"
                                                    f"Result: {self.ctx.author.mention} **WON!**")
            
        self.stop()

    @button(label = "Scissors", style = discord.ButtonStyle.green, emoji = "✂️")
    async def scissors_callback(self, interaction: discord.Interaction, button: button) -> None:

        if self.author_choice == "Rock":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Rock**\n"
                                                    f"{self.user.mention} chose: **Scissors**\n\n"
                                                    f"Result: {self.ctx.author.mention} **WON!**")
            
        elif self.author_choice == "Paper":
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Paper**\n"
                                                    f"{self.user.mention} chose: **Scissors**\n\n"
                                                    f"Result: {self.user.mention} **WON!**")
            
        else:
            await interaction.response.send_message(f"{self.ctx.author.mention} chose: **Scissors**\n"
                                                    f"{self.user.mention} chose: **Scissors**\n\n"
                                                    f"Result: **IT'S A TIE!**")
            
        self.stop()

class MultiPlayerAuthorRPS(View):

    def __init__(self, ctx: commands.Context, user: discord.Member) -> None:
        
        super().__init__(timeout = 120)
        self.ctx = ctx
        self.user = user

    async def on_timeout(self) -> None:

        for button in self.children:
            button.disabled = True
        
        await self.message.edit(view = self)
        await self.message.reply("The buttons have been disabled due to inactivity!")

    async def interaction_check(self, interaction: discord.Interaction) -> bool:

        if interaction.user != self.ctx.author:
            await interaction.response.send_message("Hey! Those options are not for you buddy", ephemeral = True)
            return False
        
        else:
            for button in self.children:
                button.disabled = True
        
            await self.message.edit(view = self)
            return True
        
    @button(label = "Rock", style = discord.ButtonStyle.green, emoji = "🪨")
    async def rock_callback(self, interaction: discord.Interaction, button: button) -> None:

        await interaction.response.defer()

        author_choice = "Rock"
        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, author_choice)
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()

    @button(label = "Paper", style = discord.ButtonStyle.green, emoji = "📰")
    async def paper_callback(self, interaction: discord.Interaction, button: button) -> None:

        await interaction.response.defer()

        author_choice = "Paper"
        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, author_choice)
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()

    @button(label = "Scissors", style = discord.ButtonStyle.green, emoji = "✂️")
    async def scissors_callback(self, interaction: discord.Interaction, button: button) -> None:

        await interaction.response.defer()

        author_choice = "Scissors"
        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, author_choice)
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()