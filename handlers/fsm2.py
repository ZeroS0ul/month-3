# from aiogram import Router
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.types import Message


# router = Router()


# class MovieForm(StatesGroup):
#     title = State()
#     genre = State()
#     rating = State()


# @router.message(Command("form"))
# async def start_form(message: Message, state: FSMContext):
#     await state.set_state(MovieForm.title)
#     await message.answer("Добавим фильм.\nВведите название фильма:")


# @router.message(Command("cancel"))
# async def cancel_form(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("Анкета отменена.")


# @router.message(MovieForm.title)
# async def get_title(message: Message, state: FSMContext):
#     await state.update_data(title=message.text)
#     await state.set_state(MovieForm.genre)
#     await message.answer("Введите жанр фильма:")


# @router.message(MovieForm.genre)
# async def get_genre(message: Message, state: FSMContext):
#     await state.update_data(genre=message.text)
#     await state.set_state(MovieForm.rating)
#     await message.answer("Введите оценку фильма от 1 до 10:")


# @router.message(MovieForm.rating)
# async def get_rating(message: Message, state: FSMContext):
#     if not message.text.isdigit():
#         await message.answer(
#             "Оценка должна быть числом от 1 до 10. Попробуйте ещё раз:"
#         )
#         return

#     rating = int(message.text)

#     if not 1 <= rating <= 10:
#         await message.answer(
#             "Оценка должна быть от 1 до 10. Попробуйте ещё раз:"
#         )
#         return

#     await state.update_data(rating=rating)

#     data = await state.get_data()

#     await message.answer(
#         "Фильм добавлен.\n\n"
#         f"Название: {data['title']}\n"
#         f"Жанр: {data['genre']}\n"
#         f"Оценка: {data['rating']}/10"
#     )

#     await state.clear()