from discord.ext import commands
from auxiliar_functions import stats_update, stats_validator


class Intelligence(commands.Cog):
    """ Commands to Increase Intelligence"""

    login = None
    champion_selected = None
    response = None
    data = None

    def __init__(self, bot):
        self.bot = bot

    @property
    def login(self):
        return getattr(self.bot, "login_instance", None)

    @commands.command(name="estudo", help="Adiciona horas de estudo. Argumentos: número de horas estudando")
    async def add_study(self, ctx, study):
        if await stats_validator(ctx, study, 15, self.login):
            stats_update(
                'study', study, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {study}h em horas de estudo")

    @commands.command(name="leitura", help="Adiciona horas de leitura. Argumentos: número de horas lendo")
    async def add_read(self, ctx, read):
        if await stats_validator(ctx, read, 5, self.login):
            stats_update(
                'reading', read, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {read}h em horas de leitura")

    @commands.command(name="meditaçao", help="Adiciona horas de meditação. Argumentos: número de horas meditando")
    async def add_meditation(self, ctx, meditation):
        if await stats_validator(ctx, meditation, 5, self.login):
            stats_update(
                'meditation', meditation, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {meditation}h em horas de meditação")


async def setup(bot):
    await bot.add_cog(Intelligence(bot))
