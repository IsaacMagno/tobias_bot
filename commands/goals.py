from discord.ext import commands
from decouple import config
import requests


class Goals(commands.Cog):
    """ Commands to Increase Strength"""

    BASE_URL = config("BASE_URL")
    login = None

    def __init__(self, bot):
        self.bot = bot

    @property
    def login(self):
        return getattr(self.bot, "login_instance", None)

    @commands.command(name="metas", help="Atualiza ou adiciona metas do campeão. Argumentos: nenhum")
    async def goals_manager(self, ctx):
        if not self.login:
            await ctx.send("Você não fez o login!")
        else:
            options_message = ('Selecione uma das opções:\n'
                               'a) Adicionar meta\n'
                               'b) Atualizar meta\n'
                               'c) Visualizar metas\n'
                               'd) Sair')

            await ctx.send(options_message)

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            response = await self.bot.wait_for('message', check=check)

            while True:
                if response.content.lower() == 'a':
                    await ctx.send('Você selecionou a opção de adicionar uma meta')
                    await ctx.send("Informe o nome e a quantidade anual da meta")

                    response = await self.bot.wait_for('message', check=check)

                    content = response.content.split()

                    data = {'name': content[0], 'type': 'Anual', 'goal': content[1],
                            'champion_id': self.login.champion_selected['id']}

                    try:
                        requests.post(f'{self.BASE_URL}/task', json=data)
                        await ctx.send("Nova meta adicionado com sucesso!")
                    except Exception as error:
                        await ctx.send("Opa, algo deu errado")
                        print(error)
                    break
                elif response.content.lower() == 'b':
                    await ctx.send('Você selecionou a opção de atualizar uma meta')
                    await ctx.send("Selecione uma das metas pelo nome e informe a quantidade")

                    response = await self.bot.wait_for('message', check=check)
                    content = response.content.split()

                    task_filtered = filter(lambda task: task['name'].lower() == content[0].lower()
                                           and task['champion_id'] == self.login.champion_selected['id'],
                                           self.login.champion_selected['task'])

                    task_id = list(map(lambda task: task['id'], task_filtered))

                    if not task_id:
                        await ctx.send("Meta não encontrada! Verifique as suas metas selecionando a opção C")
                        break

                    data = {
                        'id': task_id[0], 'actual': content[1]}

                    try:
                        requests.put(
                            f'{self.BASE_URL}/task/{task_id[0]}', json=data)
                        await ctx.send("Meta atualizada com sucesso!")
                    except Exception as error:
                        await ctx.send("Opa, algo deu errado")
                        print(error)

                    break
                elif response.content.lower() == 'c':
                    await ctx.send('Essas são as suas metas atuais:')
                    for meta in self.login.champion_selected['task']:
                        await ctx.send(f"Nome: {meta['name']}\n"
                                       f"Tipo: {meta['type']}\n"
                                       f"Objetivo: {meta['goal']}\n"
                                       f"Mensal: {meta['month']}\n"
                                       f"Semanal: {meta['week']}\n"
                                       f"Atual: {meta['actual']}")

                    break
                elif response.content.lower() == 'd':
                    await ctx.send('Saindo do gerenciamento de metas')
                    break
                else:
                    await ctx.send(f'Opção inválida. {options_message}')


async def setup(bot):
    await bot.add_cog(Goals(bot))
