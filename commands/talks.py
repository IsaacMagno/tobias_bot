from discord.ext import commands
import requests
from bs4 import BeautifulSoup

from random import randint


class Talks(commands.Cog):
    """ Talks with user"""
    aleat_phrase = []
    saudacao = ["Foco guerreiro ",
                "Pra cima ",
                "Bora lá ",
                "Força cabrone ",
                "Arregaça tudo ",
                "Acaba com eles "]

    def __init__(self, bot):
        self.bot = bot

    def get_phrase(self, request):
        data = request.text
        bs = BeautifulSoup(data, "html.parser")

        phrases = bs.findAll("p", {"class": "frase fr0"})
        phrases_2 = bs.findAll("p", {"class": "frase fr"})

        for phrase in phrases:
            text = phrase.text
            self.aleat_phrase.append(text.strip())

        for phrase in phrases_2:
            text = phrase.text
            self.aleat_phrase.append(text.strip())

    @commands.command(name="motivaçao", help="Gera uma frase aleatoria pra dar aquele gás! (ou não).")
    async def send_motivation(self, ctx):
        try:
            randindex = randint(0, 3890)
            request = requests.get(
                f"https://www.pensador.com/motivacao/{randindex}")

            if request.status_code == 200:
                self.get_phrase(request)
            else:
                self.aleat_phrase.append(
                    "Falha ao gerar frase, tente novamente!")

            randindex = randint(0, len(self.aleat_phrase) - 1)

            name = ctx.author.name

            response = f"{self.saudacao[randint(0, len(self.saudacao) - 1)]}{name}!\n\n{self.aleat_phrase[randindex]}"

            await ctx.send(response)
        except Exception as error:
            await ctx.send(f"Opa, calma ae to pensando melhor...")
            print(error)


async def setup(bot):
    await bot.add_cog(Talks(bot))
