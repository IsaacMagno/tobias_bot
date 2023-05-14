from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from discord.ext import commands


class Manager(commands.Cog):
    """Manage the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Energizado e pronto para servir!")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando não encontrado! Utilize '!help' para mais informações")
        elif isinstance(error, MissingRequiredArgument):
            await ctx.send("Argumentos faltando! Utilize '!help' para mais informações")
        else:
            raise error


async def setup(bot):
    await bot.add_cog(Manager(bot))
