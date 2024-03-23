import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from wiki import wikipedia


TOKEN = "7161366443:AAG5TTiEBorRpZpwKFJ7mwEfrAxkT4h8SO8"
dp = Dispatcher()

@dp.message(Command(commands="help"))
async def command_help_handler(message: Message) -> None:
    
    text = "Bot commands\n /start-run the bot\n"
    await message.reply(text)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Salom, {full_name}\n Bu bot wikipediadek ishlaydi>>> "

    await message.reply(text=text)

@dp.message()
async def sendWikki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

