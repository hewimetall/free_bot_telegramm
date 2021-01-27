"""Сервер Telegram бота, запускаемый непосредственно"""
import logging
from aiogram import Bot, Dispatcher, executor

logging.basicConfig(level=logging.INFO)

API_TOKEN = "1587078195:AAEIPrGErBtyufm4PXsFyMnqfEgszYOg5G4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

from handler.comand import *
from handler.common_type import *

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)