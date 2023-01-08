from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
first=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Button 1',callback_data='second')]
    ]
)
kb=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1',callback_data='b1')],
        [InlineKeyboardButton(text='2',callback_data='b2')],
        [InlineKeyboardButton(text='3',callback_data='b3')]
    ]
)