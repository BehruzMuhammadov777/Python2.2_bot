from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

ichimliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pepsi"),
            KeyboardButton(text="Fanta")
        ],
        [
            KeyboardButton(text="Cocacola"),
            KeyboardButton(text="7-up"),
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)