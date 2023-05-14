from discord.ext import commands
from auxiliar_functions import stats_update, stats_validator


class Strength(commands.Cog):
    """ Commands to Increase Strength"""

    login = None
    champion_selected = None
    response = None
    data = None

    def __init__(self, bot):
        self.bot = bot

    @property
    def login(self):
        return getattr(self.bot, "login_instance", None)

    @commands.command(name="flexao", help="Adiciona treino superior. Argumentos: número de treino superior")
    async def add_push_up(self, ctx, push_up):
        if await stats_validator(ctx, push_up, 450, self.login):
            stats_update(
                'upperLimb', push_up, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {push_up} em treino superior")

    @commands.command(name="abdominal", help="Adiciona treino abdominal. Argumentos: número de abdominais")
    async def add_abs(self, ctx, abs):
        if await stats_validator(ctx, abs, 450, self.login):
            stats_update(
                'abs', abs, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {abs} em treino abdominal")

    @commands.command(name="pernas", help="Adiciona treino inferior. Argumentos: número de treino inferior")
    async def add_lower(self, ctx, lower):
        if await stats_validator(ctx, lower, 450, self.login):
            stats_update(
                'lowerLimb', lower, self.login.champion_selected["id"])
            await ctx.send(f"Adicionado {lower} em treino inferior")


async def setup(bot):
    await bot.add_cog(Strength(bot))
