from discord.ext import commands
import requests
from decouple import config
from auxiliar_functions import selected_champion


class Login(commands.Cog):
    """ Commands to Login"""

    champion_selected = None
    data = None
    login = False
    BASE_URL = config("BASE_URL")

    def __init__(self, bot):
        self.bot = bot
        request = requests.get(self.BASE_URL)
        self.data = request.json()

    @commands.command(name="login", help="Faz o login. Argumentos: usuário e senha")
    async def login(self, ctx, username, password):
        data = {"username": username, "password": password}

        await ctx.message.delete()

        request = requests.post(
            f"{self.BASE_URL}/champion-login", json=data)

        self.login = request.json()

        if self.login["validLogin"] == True:
            self.champion_selected = selected_champion(
                username, self.data["champions"])
            self.bot.login_instance = self
            await ctx.send(f"Bem vindo {username}")
        else:
            await ctx.send("Login ou senha incorretos!")


async def setup(bot):
    await bot.add_cog(Login(bot))
