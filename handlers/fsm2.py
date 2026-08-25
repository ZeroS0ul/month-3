from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from db.homework_db import add_movie, get_movies


router = Router()


class MovieForm(StatesGroup):
    title = State()
    genre = State()
    rating = State()


@router.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(MovieForm.title)
    await message.answer("Введите название фильма:")


@router.message(Command("cancel"))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Анкета отменена.")


@router.message(MovieForm.title)
async def get_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)

    await state.set_state(MovieForm.genre)
    await message.answer("Введите жанр фильма:")


@router.message(MovieForm.genre)
async def get_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)

    await state.set_state(MovieForm.rating)
    await message.answer("Введите оценку от 1 до 10:")


@router.message(MovieForm.rating)
async def get_rating(message: Message, state: FSMContext):
    try:
        rating = float(message.text.replace(",", "."))
    except ValueError:
        await message.answer("Оценка должна быть числом.")
        return

    if not 1 <= rating <= 10:
        await message.answer("Оценка должна быть от 1 до 10.")
        return

    data = await state.get_data()

    add_movie(
        data["title"],
        data["genre"],
        rating
    )

    await message.answer(
        f"Фильм сохранён.\n\n"
        f"Название: {data['title']}\n"
        f"Жанр: {data['genre']}\n"
        f"Оценка: {rating}"
    )

    await state.clear()


@router.message(Command("movies"))
async def show_movies(message: Message):
    movies = get_movies()

    if not movies:
        await message.answer("В базе пока нет фильмов.")
        return

    text = "Фильмы из базы:\n\n"

    for movie in movies:
        text += (
            f"{movie[0]}. {movie[1]}\n"
            f"Жанр: {movie[2]}\n"
            f"Оценка: {movie[3]}\n\n"
        )

    await message.answer(text)