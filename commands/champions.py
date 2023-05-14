from discord.ext import commands
import requests
from decouple import config
from auxiliar_functions import selected_champion


class Champions(commands.Cog):
    """ Get info from champions"""

    champion_list = []
    response = None
    data = None
    BASE_URL = config("BASE_URL")
    champion_selected = None
    translation_dict = {
        "strength": "Força",
        "agility": "Agilidade",
        "inteligence": "Inteligencia",
        "vitality": "Vitalidade",
        "wisdow": "Sabedoria",
        "kmRun": "Km Corridos",
        "jumpRope": "Saltos de Corda",
        "kmBike": "Km Bike",
        "upperLimb": "Flexoes",
        "abs": "Abdominais",
        "lowerLimb": "Pernas",
        "meals": "Refeições",
        "drinks": "Litros de Agua",
        "sleep": "Horas Dormindo",
        "study": "Horas Estudando",
        "meditation": "Horas Meditando",
        "reading": "Horas Lendo"
    }

    def __init__(self, bot):
        self.bot = bot
        self.response = requests.get(self.BASE_URL)
        self.data = self.response.json()

    async def champions_request(self, ctx):
        await ctx.send("Estou verificando o banco de dados")

        self.response = requests.get(self.BASE_URL)
        self.data = self.response.json()

    def format_statistics(self, statistics):
        message = '     Estatísticas\n'

        statistics = dict((self.translation_dict[key], statistics[key]) for key in (
            'strength', 'agility', 'inteligence', 'vitality', 'wisdow'))

        for key, value in statistics.items():
            message += f'           {key}: {value}\n'

        return message

    def format_activities(self, activities):
        message = '     Características\n'

        activities = dict((self.translation_dict[key], activities[key]) for key in (
            "kmRun", "jumpRope", "kmBike", "upperLimb", "abs", "lowerLimb", "meals", "drinks", "sleep", "study", "meditation", "reading"))

        for key, value in activities.items():
            message += f'           {key}: {value}\n'

        return message

    def message_formater(self, champion):
        formated_message = f'Nome: {champion["name"]}\n'

        formated_message += self.format_statistics(
            champion["statistics"])

        formated_message += self.format_activities(
            champion["activities"])

        return formated_message

    @commands.command(name="champs", help="Mostra os atuais campeões cadastrados. Argumentos: Nenhum")
    async def get_champions(self, ctx):
        try:
            await self.champions_request(ctx)
            ctx_message = []

            for champion in self.data["champions"]:
                ctx_message.append(self.message_formater(champion))

            for message in ctx_message:
                await ctx.send(message)

            ctx_message = []

        except Exception as error:
            await ctx.send(f"Opa, calma ae to pensando melhor...")
            print(error)

    @commands.command(name="champ", help="Mostra o campeão de acordo com o nome. Argumentos: Nome do campeão")
    async def get_champion(self, ctx, champion_name):
        try:
            await self.champions_request(ctx)

            champion_selected = selected_champion(
                champion_name, self.data["champions"])

            await ctx.send(self.message_formater(champion_selected))

        except Exception as error:
            await ctx.send(f"Aconteceu alguma coisa errada... Tente novamente")
            print(error)


async def setup(bot):
    await bot.add_cog(Champions(bot))
