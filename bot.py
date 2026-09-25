import asyncio
import datetime
import os
from threading import Thread
import discord
from discord.ext import commands, tasks
from flask import Flask

# Веб-сервер для поддержки активности Render 24/7
app = Flask('')


@app.route('/')
def home():
    return 'Бот работает!'


def run_web():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    Thread(target=run_web).start()


# Указываем часовой пояс UTC+5
TZ_UTC5 = datetime.timezone(datetime.timedelta(hours=5))

# --- НАСТРОЙКИ ---
TOKEN = os.getenv('TOKEN')
CHANNEL_ID = 123456789012345678  # Укажите ваш ID канала
MENTION = '<@ne_lordylol_59426> <@nonker.>'  # Ваши теги или @everyone
ALARM_TIMES = ['15:00']  # Время срабатывания (по UTC+5)
# -----------------

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен.')
    alarm_loop.start()


@tasks.loop(seconds=30)
async def alarm_loop():
    # Берём время именно по поясу UTC+5
    now = datetime.datetime.now(TZ_UTC5).strftime('%H:%M')

    if now in ALARM_TIMES:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send(
                f'{MENTION}, Время лизать пизду, мальчики🥰'
            )
            await asyncio.sleep(60)


keep_alive()
bot.run(TOKEN)