from aiogram.types import  ReplyKeyboardMarkup,KeyboardButton

fastfood_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Burger")
        ],
        [
            KeyboardButton(text="Shaurma"),
            KeyboardButton(text="Xot-dog"),
            KeyboardButton(text="Ortga"),

        ]
    ],
    resize_keyboard=True
)