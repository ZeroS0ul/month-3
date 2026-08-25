

from aiogram import Bot
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery

from handlers.buttons import main_buttons, main_builder, menu_inline, product_actions
from db import main_db

router_commands = Router()


@router_commands.message(Command('start'))
async def start_command(message: Message, bot: Bot):
    await message.answer('Привет. Напиши своё имя ', reply_markup=menu_inline)
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет. Твой ID - {message.from_user.id}'
    )


@router_commands.message(Command('help'))
async def help_command(message: Message):
    await message.answer('/start - старт бота \n/help - помощник')


@router_commands.callback_query(F.data == 'help')
async def cmd_help_inline(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer('/start - старт бота \n/help - помощник')


@router_commands.message(F.text == 'привет')
async def hello_command(message: Message):
    await message.answer('Hello')


@router_commands.message(Command('mem'))
async def mem_command(message: Message, bot: Bot):
    photo = FSInputFile('media/mem.png')
    await message.answer_photo(photo=photo)


@router_commands.callback_query(F.data == 'mem')
async def mem_command_inline(call: CallbackQuery, bot: Bot):
    await call.answer()
    photo = FSInputFile('media/mem.png')
    await call.message.answer_photo(photo=photo)


@router_commands.message(Command('products'))
async def get_products(message: Message):
    products = await main_db.get_product_db()
    if not products:
        await message.answer('В базе товаров нет!')
        return
    else:
        for name, price, category, description, product_id, photo_id in products:
            await message.answer_photo(
                photo=photo_id,
                caption=(
                    f'Название - {name}\n'
                    f'Цена - {price}\n'
                    f'Описание - {description}\n'
                    f'Категория - {category}\n'
                    f'Артикул - {product_id}'
                ),
                reply_markup=product_actions(product_id=product_id)
            )