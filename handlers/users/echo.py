from keyboards.inline import first
from aiogram import types
from loader import dp
from keyboards.default import phone
from states import Flow

@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def bot_echo(message:types.Message):
    if message.contact.user_id != message.from_id:
        await message.answer(f'wrong data,retry')
    else:
        await Flow.RegisterState.set()
        await message.answer(f'wellcum{message.from_user.full_name}')


@dp.message_handler(commands=['Info'])
async def bot_echo(message: types.Message):
    await message.answer(f'{message.from_user.full_name},{message.from_user.language_code}',reply_markup=first)

@dp.message_handler(commands=['use'])
async def bot_echo(message:types.Message):
    await message.answer(f'for using our both provide your phone number',reply_markup=phone)


@dp.message_handler(content_types=types.ContentTypes.STICKER)
async def bot_echo(message:types.Message):
    await message.answer_sticker(f'{message.sticker.file_id}')




