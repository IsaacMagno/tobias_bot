from discord.ext import commands
from auxiliar_functions import stats_update, stats_validator


class Vitality(commands.Cog):
    """ Commands to Increase Vitality"""

    login = None

    def __init__(self, bot):
        self.bot = bot

    @property
    def login(self):
        return getattr(self.bot, "login_instance", None)

    @commands.command(name="refeiçao", help="Adiciona refeições saudáveis. Argumentos: número de refeições")
    async def add_meals(self, ctx, meals):
        if await stats_validator(ctx, meals, 8, self.login):
            stats_update(
                'meals', meals, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {meals} em refeições saudáveis")

    @commands.command(name="agua", help="Adiciona litros de água. Argumentos: número de litros")
    async def add_drinks(self, ctx, drinks):
        if await stats_validator(ctx, drinks, 5, self.login):
            stats_update(
                'drinks', drinks, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {drinks}L em litros de água")

    @commands.command(name="sono", help="Adiciona horas de sono. Argumentos: número de horas de sono")
    async def add_sleep(self, ctx, sleep):
        if await stats_validator(ctx, sleep, 12, self.login):
            stats_update(
                'sleep', sleep, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {sleep}h em horas de sono")


async def setup(bot):
    await bot.add_cog(Vitality(bot))
