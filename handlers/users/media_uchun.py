from aiogram import types
from aiogram.types import ContentTypes, InputFile

from loader import dp, bot


# Echo bot
@dp.message_handler(content_types=ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.photo[-1].download()
    await message.answer(text="Rasm qabul qilindi")


@dp.message_handler(text="Soup")
async def bot_echo(message: types.Message):
  rasm_manzili = "https://t.me/media_uchun596/16"
  user_id = message.from_user.id

  await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Osh\n"
                       "Narxi : 20 000 so'm")


@dp.message_handler(text="Shorva")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/13"
    user_id = message.from_user.id

    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Shorva\n"
                         "Narxi : 12 000 so'm")


@dp.message_handler(text="Mastava")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/9"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu mastava\n"
                         "Narxi : 15 000 so'm")


@dp.message_handler(text="SShashlik")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/17"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu SShashlik\n"
                         "Narxi : 11 000 so'm")


@dp.message_handler(text="Tort")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/15"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Tort\n"
                         "Narxi : 70 000 so'm")


@dp.message_handler(text="Baklava")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/11"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Paxlava\n"
                         "Narxi : 55 000 so'm")



@dp.message_handler(text="Roulette")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/7"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Rulet\n"
                         "Narxi : 65 000 so'm")



@dp.message_handler(text="cake")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/11"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Kekis\n"
                         "Narxi :150 000 so'm")


@dp.message_handler(text="Cocacola")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/8"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Cocacola\n"
                         "Narxi :15 000 so'm")


@dp.message_handler(text="Fanta")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/18"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Fanta\n"
                         "Narxi :13 000 so'm")



@dp.message_handler(text="Pepsi")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/19"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Pepsi\n"
                         "Narxi :12 000 so'm")



@dp.message_handler(text="7-up")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/20"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu 7-up\n"
                         "Narxi :13 000 so'm")


@dp.message_handler(text="Burger")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/6"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Burger\n"
                         "Narxi :24 000 so'm")


@dp.message_handler(text="Xot-dog")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/3"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Xot-dog\n"
                         "Narxi :20 000 so'm")


@dp.message_handler(text="Lavash")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/23"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Lavash\n"
                         "Narxi :22 000 so'm")


@dp.message_handler(text="Shaurma")
async def bot_echo(message: types.Message):
    rasm_manzili = "https://t.me/media_uchun596/25"
    user_id = message.from_user.id


    await bot.send_photo(chat_id=user_id,photo=rasm_manzili,caption="Bu Shaurma\n"
                         "Narxi :20 000 so'm")




