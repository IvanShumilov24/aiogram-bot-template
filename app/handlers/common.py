from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("start"))
async def profile_handler(
        message: Message,
):
    await message.answer("ТАК НАХУЙ, ДОБРО ПОЖАЛОВАТЬ В НАШУ КАЧАЛКУ\n\nТУТ МЫ УЧИМ МУЖИКОВ КАК ПРАВИЛЬНО ТЯГАТЬ КОД СИДЯ, ПРОЕКТИРОВАТЬ БЕЛКОВУЮ АРХИТЕКТУРУ И НАРАЩИВАТЬ ТЕСТОВУЮ МАССУ")
