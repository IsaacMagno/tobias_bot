from discord.ext import commands
from auxiliar_functions import stats_update, stats_validator


class Agility(commands.Cog):
    """ Commands to Increase Agility"""

    login = None
    champion_selected = None
    response = None
    data = None

    def __init__(self, bot):
        self.bot = bot

    @property
    def login(self):
        return getattr(self.bot, "login_instance", None)

    @commands.command(name="corrida", help="Adiciona quilômetros corridos. Argumentos: número de quilômetros")
    async def add_km_run(self, ctx, km_run):
        if await stats_validator(ctx, km_run, 20, self.login):
            stats_update(
                'kmRun', km_run, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {km_run}Km em quilômetros corridos")

    @commands.command(name="saltos", help="Adiciona saltos de corda. Argumentos: número de saltos")
    async def add_jumps(self, ctx, jumps):
        if await stats_validator(ctx, jumps, 500, self.login):
            stats_update(
                'jumpRope', jumps, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {jumps} saltos de corda")

    @commands.command(name="bike", help="Adiciona quilômetros pedalados. Argumentos: número de quilômetros")
    async def add_km_bike(self, ctx, km_bike):
        if await stats_validator(ctx, km_bike, 20, self.login):
            stats_update(
                'kmBike', km_bike, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {km_bike}Km em quilômetros pedalados")


async def setup(bot):
    await bot.add_cog(Agility(bot))
