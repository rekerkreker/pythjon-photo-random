import os
import logging
import random
from random import choice
import json
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN= '5485255207:AAEPMHtr1dJPAz82t1EYeNbl8-hicVG7yOU'

keywords = {'pics':{'картинка','картинку','картинки'}, 'people':{'люди','человек','людей','человека'} ,'space':{'космоса','космос','space'} ,'nature':{'природы','природа' ,'растения'} }

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer('Привет! Я бот для работы с фотографиями. Вы можете найти фотографию по ключевому слову. \n по запросам картинка людей \n картинка природы \n космоса')


@dp.message_handler()
async def program(message: types.Message):
    if set(message.text.split()).intersection(keywords['pics']):
        print('1')
        categories = list(keywords.keys())
        categories.remove('pics')
        for category in categories:
            if set(message.text.split()).intersection(keywords[category]):
                print('2')
                base_path = f'images/{category}/'
                pic_path = base_path + random.choice(os.listdir(base_path))
                pic = open(pic_path, 'rb')
                await bot.send_photo(message.chat.id, pic, f'Вот тебе {category}')
    else:
        await message.answer('Что то сломалось 404')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)