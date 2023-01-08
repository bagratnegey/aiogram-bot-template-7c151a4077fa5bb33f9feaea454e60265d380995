from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default import phone
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")

@dp.message_handler(CommandStart)
async def bot_echo(message:types.Message):
    await message.answer(f'for using this porvide phone number',reply_markup=phone)
