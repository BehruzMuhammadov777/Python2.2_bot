from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tort"),
            KeyboardButton(text="Roulette")
        ],
        [
            KeyboardButton(text="cake"),
            KeyboardButton(text="Baklava"),
            KeyboardButton(text='Ortga')
        ]
    ],
    resize_keyboard=True
)