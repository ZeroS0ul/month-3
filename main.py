from aiogram import Bot,Dispatcher
import logging
from config import bot_token, admin
import asyncio
from handlers import command, echo, fsm, fsm_edit
from db import main_db
from aiogram.types import BotCommand

bot = Bot(token=bot_token)
dp = Dispatcher()

async def set_commands():
    commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='Помощь'),
        BotCommand(command='mem', description='мем'),
        BotCommand(command='products', description='Получить товары из БД'),
        BotCommand(command='add_product', description='Записать товар'),
    ]
    await bot.set_my_commands(commands)


async def on_startup():
    await main_db.init_db()
    await set_commands()
    for admin_id in admin:
        await bot.send_message(chat_id=admin_id, text='Бот включен!')

dp.include_router(command.router_commands)
dp.include_router(fsm.router_fsm)
dp.include_router(fsm_edit.router_edit)


dp.include_router(echo.router_echo)

dp.startup.register(on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))