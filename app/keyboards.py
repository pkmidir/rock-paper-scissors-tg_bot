from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

rsp = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🪨 Камень' , callback_data='rock'),
     InlineKeyboardButton(text='✂️Ножницы' , callback_data='scissors')],
    [InlineKeyboardButton(text='🧻Бумага', callback_data='paper')]
])