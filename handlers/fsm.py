from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from db import main_db

router_fsm = Router()

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()
    product_id = State() 
    category = State()
    photo = State()


@router_fsm.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товара:')
    await state.set_state(AddProduct.name)

@router_fsm.message(AddProduct.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара')
    await state.set_state(AddProduct.price)

@router_fsm.message(AddProduct.price)
async def add_price(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer('Цена должна быть числом. Попробуйте еще раз')
    else:
        await state.update_data(price=message.text)
        await message.answer('Введите описание для данного товара:')
        await state.set_state(AddProduct.description)

@router_fsm.message(AddProduct.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Введите артикул для товара. Он должен быть уникальным!')
    await state.set_state(AddProduct.product_id)

@router_fsm.message(AddProduct.product_id)
async def add_product_id(message: Message, state: FSMContext):
    await state.update_data(product_id=message.text)
    await message.answer('Введите категорию')
    await state.set_state(AddProduct.category)

@router_fsm.message(AddProduct.category)
async def add_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer('Отправьте фото товара')
    await state.set_state(AddProduct.photo)


@router_fsm.message(AddProduct.photo, F.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()

    # await message.answer(
    #     f"Товар добавлен!\n"
    #     f"Название товара - {data['name']}\n"
    #     f"Цена: {data['price']}\n"
    #     f"Описание: {data['description']}\n"
    #     f"Артикул: {data['product_id']}\n"
    #     f"Категория: {data['category']}"
    # )

    await message.answer_photo(photo=data['photo'], caption=(f"Товар добавлен!\n"
        f"Название товара - {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}\n"
        f"Артикул: {data['product_id']}\n"
        f"Категория: {data['category']}")
    )

    await main_db.add_product_db(name_product=data['name'], price=data['price'], product_id=data['product_id'], photo_id=data['photo'])

    await main_db.add_product_detail_db(product_id=data['product_id'], category=data['category'], description=data['description'])

    await state.clear()
