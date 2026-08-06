from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import random
from datetime import datetime

TOKEN = "8870211815:AAHF91yYldY_7iaJMt1KuOwU9J55xIyF-Vc"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот.")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(
        "/start - запуск бота\n"
        "/help - помощь\n"
        "/time - текущее время\n"
        "/random - случайное число\n"
        "/joke - случайная шутка"
    )


@dp.message(Command("time"))
async def time(message: Message):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    await message.answer(f"Сейчас: {now}")


@dp.message(Command("random"))
async def random_number(message: Message):
    number = random.randint(1, 100)
    await message.answer(f"Твоё случайное число: {number}")


@dp.message(Command("joke"))
async def joke(message: Message):
    jokes = [
        "Программист не ошибается, он тестирует.",
        "Баг — это неожиданная возможность.",
        "Python любит отступы!",
        "Компьютер тоже иногда устает.",
        "Кофе — лучший друг программиста."
    ]
    await message.answer(random.choice(jokes))


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())