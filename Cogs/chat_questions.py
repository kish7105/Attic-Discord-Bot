import random
from Configs.basic_utils import interesting_questions

from discord.ext import commands, tasks

class ChatQuestions(commands.Cog):
    
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.cooldown = False
        self.general_channel_id = 1202305993954828292
        self.printer.start()

    def cog_unload(self) -> None:
        self.printer.cancel()

    @tasks.loop(hours = 1)
    async def printer(self):
        channel = self.client.get_channel(self.general_channel_id)
        await channel.send(random.choice(interesting_questions))

    @printer.before_loop
    async def before_printer(self) -> None:
        print("waiting for the bot to start...")
        await self.client.wait_until_ready()

async def setup(client: commands.Bot) -> None:
    await client.add_cog(ChatQuestions(client))