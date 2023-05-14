import requests
from decouple import config

BASE_URL = config("BASE_URL")


def stats_update(statsName, statsValue, id):
    try:
        requests.put(
            f"{BASE_URL}/activities/{int(id)}", json={statsName: int(statsValue)})
    except Exception as error:
        print(error)


def selected_champion(username, champions):
    selected = filter(
        lambda champion: champion["name"].lower() == username, champions)
    selected_list = list(selected)

    if len(selected_list):
        return selected_list[0]
    else:
        return "Nenhum campeão com esse nome encontrado!"


async def stats_validator(ctx, stats_value, max_value, login):
    if not login:
        await ctx.send("Você não fez o login!")
        return False
    elif not stats_value:
        await ctx.send("Você precisa me informar o valor!")
        return False
    elif not stats_value.isdigit():
        await ctx.send("O valor precisa ser composto por números e ser positivo!")
        return False
    elif int(stats_value) > max_value:
        await ctx.send("O valor é alto demais!")
        return False
    elif int(stats_value) == 0:
        await ctx.send("O valor precisa ser maior que zero!")
        return False
    else:
        return True
