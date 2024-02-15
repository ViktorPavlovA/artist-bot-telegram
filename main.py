
import asyncio
import logging
import sys
from os import getenv
import yaml
from aiogram.filters import Filter



from aiogram import Bot, Dispatcher, Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message 
from aiogram.utils.markdown import hbold
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

FLAG_DEBUG = True

dp = Dispatcher()
router = Router()


# Создание клавиатуры
main_kb = InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text = "📝FAQ", callback_data="faq"),
InlineKeyboardButton(text = "‼️event‼️", callback_data="event"),
InlineKeyboardButton(text = "👥profile", callback_data="prof")
]
],)



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """

    await message.answer(f"{config['init_message']}, {message.from_user.first_name}😊")

@dp.message(F.text, Command("menu"))
async def any_message(message: Message):
    await message.answer("test", reply_markup=main_kb)



async def main(config:dict) -> None:
    bot = Bot(config['api_key'])
    await dp.start_polling(bot)

if __name__ == '__main__':
    with open('cfg/config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    asyncio.run(main(config))





