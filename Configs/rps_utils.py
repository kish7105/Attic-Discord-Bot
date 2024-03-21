import random

import discord
from discord.ext import commands
from discord.ui import View, button

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

        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, "Rock")
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()

    @button(label = "Paper", style = discord.ButtonStyle.green, emoji = "📰")
    async def paper_callback(self, interaction: discord.Interaction, button: button) -> None:

        await interaction.response.defer()

        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, "Paper")
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()

    @button(label = "Scissors", style = discord.ButtonStyle.green, emoji = "✂️")
    async def scissors_callback(self, interaction: discord.Interaction, button: button) -> None:

        await interaction.response.defer()

        mrps_user_view = MultiPlayerUserRPS(self.ctx, self.user, "Scissors")
        mrps_user_view.message = await self.ctx.send(f"{self.user.mention}\n"
                                                                         "Choose Rock, Paper or Scissors!",
                                                                         view = mrps_user_view)
        
        self.stop()