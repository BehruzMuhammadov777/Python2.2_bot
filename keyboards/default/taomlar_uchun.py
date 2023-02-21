from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

taomlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Soup"),
            KeyboardButton(text="SShashlik")
        ],
        [
            KeyboardButton(text="Mastava"),
            KeyboardButton(text="Shorva"),
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)