from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

tillar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="O'zbek tili",callback_data='til1'),
            InlineKeyboardButton(text="English",callback_data='til2')
        ],
        [
            InlineKeyboardButton(text="Hamkorlarimiz",url="https://t.me/kulgili"),
            InlineKeyboardButton(text="ulashish",switch_inline_query="Bu online oshxona boti")
        ]
    ],
)