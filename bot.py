import asyncio
import datetime
import os
from threading import Thread
import discord
from discord.ext import commands, tasks
from flask import Flask

# Веб-сервер для работы на Render 24/7
app = Flask('')


@app.route('/')
def home():
    return 'Бот работает!'


def run_web():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    Thread(target=run_web).start()


# НАСТРОЙКИ
TOKEN = os.getenv('TOKEN')  # Токен добавим позже в настройках Render
CHANNEL_ID = 1549615447794520086  # Вставьте ваш ID канала
MENTION = '<@ne_lordylol_59426> <@nonker.>'  # Замените на ваши теги или @everyone
ALARM_TIMES = ['15:00']  # Время оповещений (ЧЧ:ММ)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} готова сосать ваши большие члены, мальчики🥰')
    alarm_loop.start()


@tasks.loop(seconds=30)
async def alarm_loop():
    now = datetime.datetime.now().strftime('%H:%M')
    if now in ALARM_TIMES:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(
                f'{MENTION}, Время лизать пизду, мальчики🥰'
            )
            await asyncio.sleep(60)


keep_alive()
bot.run(TOKEN)
