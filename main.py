
import asyncio
import logging
import sys
from os import getenv
import yaml
from aiogram.filters import Filter



from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message 
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


dp = Dispatcher()
router = Router()



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    kb = [
        [types.KeyboardButton(text="Для себя")],
        [types.KeyboardButton(text="В подарок")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)

    await message.answer(f"{config['init_message']}, {message.from_user.first_name}😊", reply_markup=keyboard)
    await message.answer("Для кого выбираете картину?")

@dp.message(F.text == "Для себя")
async def any_message(message: Message):
    kb = [
        [types.KeyboardButton(text="Пейзаж")],
        [types.KeyboardButton(text="Животные")],
        [types.KeyboardButton(text="Абстрактное искусство")],
        [types.KeyboardButton(text="Натюрморт")],
        [types.KeyboardButton(text="Цветы")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Какие предпочтения в теме картины?", reply_markup=keyboard)












@dp.message(F.text == "Помощь🛟")
async def any_message(message: Message):
    kb = [
        [types.KeyboardButton(text="Меню")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Помощь сработала", reply_markup=keyboard)



@dp.message(F.text == "Творчество🎩")
async def any_message(message: Message):
    kb = [
        [types.KeyboardButton(text="Творчество🎩")],
        [types.KeyboardButton(text="События🌠")],
        [types.KeyboardButton(text="Помощь🛟")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Помощь сработала", reply_markup=keyboard)



@dp.message(F.text == "События🌠")
async def any_message(message: Message):
    kb = [
        [types.KeyboardButton(text="Творчество🎩")],
        [types.KeyboardButton(text="События🌠")],
        [types.KeyboardButton(text="Помощь🛟")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Помощь сработала", reply_markup=keyboard)



async def main(config:dict) -> None:
    bot = Bot(config['api_key'])
    await dp.start_polling(bot)

if __name__ == '__main__':
    with open('cfg/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    asyncio.run(main(config))





