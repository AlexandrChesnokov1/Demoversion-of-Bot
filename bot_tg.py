from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TOKEN, API
from pyowm import OWM
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


button = KeyboardButton(['Москва'], ['Санкт-Петербург'])

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button)


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await message.reply('Привет!'
                        '/weather, чтобы активировать бота на поиск погоды '
                        '/add, чтобы запомнить место в быстрой панели')


@dp.message_handler(commands=['weather'])
async def weather_activate(message: types.Message):
    await message.reply('Введите название интересующего места')
    @dp.message_handler()
    async def open_weather(msg: types.Message):
            place = msg.text
            owm = OWM(API)
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(place)
            w = observation.weather
    #        print(w.temperature('celsius'))
            output = w.temperature('celsius')
            print(output)
            await msg.reply(output)


@dp.message_handler(commands=['add'])
async def add_region(message: types.Message):
    await message.reply('Введите название региона, которое хотите добавить.')
    @dp.message_handler()
    async def new_region(reg: types.Message):
        region = reg.text
        print(region)







if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
