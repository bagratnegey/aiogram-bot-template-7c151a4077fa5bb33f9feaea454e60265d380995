from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
colors=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='red'),
            KeyboardButton(text='gay'),
            KeyboardButton(text='blue',request_contact=True)
        ]
    ],
    resize_keyboard=True
)
phone=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='share your phone noombir',request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)