from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Taomlar'),
            KeyboardButton(text='Ichimliklar')
        ],
        [
            KeyboardButton(text='Shirinliklar'),
            KeyboardButton(text='Fast food'),
            KeyboardButton(text='Ortga')
        ],
        [
            KeyboardButton(text="Adminga murojaat")
        ],
        [
            KeyboardButton(text="Kontakt"),
            KeyboardButton(text="Lokatsiya")
        ]
    ],
    resize_keyboard=True
)

menu_buttons_eng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Dishes'),
            KeyboardButton(text='Drinks')
        ],
        [
            KeyboardButton(text='Sweets'),
            KeyboardButton(text='Fast food'),
            KeyboardButton(text='Back')
        ],

        [
            KeyboardButton(text="Kontakt"),
            KeyboardButton(text="Lokatsiya"),
            KeyboardButton(text='Back')

        ]
    ],
    resize_keyboard=True
)

tasdiqlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)

