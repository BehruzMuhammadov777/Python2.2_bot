from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons,menu_buttons_eng
from keyboards.default.taomlar_uchun import taomlar_buttons
from keyboards.default.ichimliklar_uchun import ichimliklar_buttons
from keyboards.default.shirinliklar_uchun import shirinliklar_buttons
from keyboards.default.fast_food import fastfood_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from loader import dp
from aiogram.types import CallbackQuery

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)


@dp.message_handler(text='Taomlar')
async def bot_start(message: types.Message):
    await message.answer(f"quyidagi taomlardan birini tanlang",reply_markup=taomlar_buttons)


@dp.message_handler(text='Ichimliklar')
async def bot_start(message: types.Message):
    await message.answer(f"quyidagi ichimliklardan birini tanlang",reply_markup=ichimliklar_buttons)


@dp.message_handler(text='Shirinliklar')
async def bot_start(message: types.Message):
    await message.answer(f"quyidagi shirinliklardandan birini tanlang",reply_markup=shirinliklar_buttons)


@dp.message_handler(text='Fast food')
async def bot_start(message: types.Message):
    await message.answer(f"quyidagi fast fooddan birini tanlang",reply_markup=fastfood_buttons)


@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    await message.answer(f"Ortga qaytish",reply_markup=menu_buttons)


@dp.callback_query_handler(text="til2")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"English language is selected",reply_markup=menu_buttons_eng)

@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"O'zbek tili tanlandi",reply_markup=menu_buttons)

