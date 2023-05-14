import os
import asyncio
import discord
from decouple import config
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


async def load_cogs(bot):
    await bot.load_extension("manager")
    # await bot.load_extension("tasks")

    for file in os.listdir("commands"):
        if file.endswith(".py"):
            cog = file[:-3]
            await bot.load_extension(f"commands.{cog}")


async def main():
    await load_cogs(bot)
    TOKEN = config("TOKEN")
    await bot.start(TOKEN)

asyncio.run(main())
