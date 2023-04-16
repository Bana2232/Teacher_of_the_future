from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputMediaPhoto
from Klava import ikb, ikbb
from Courses import mat_course, opisanie

TOKEN_API = '5927151454:AAFJHukxbmwggEEiMPFXp8Pzkh5CTaLiqcE'
HELP = '''
/start - начать работу бота
/help - вывести список доступных комманд
/courses - вывести список доступных курсов
/auth - войти в свой аккаунт'''
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

current = dict()


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    current[message.chat.id] = 0

    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать, ознакомьтесь списком возможностей коммандой "
                                "/help")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP)


@dp.message_handler(commands=['courses'])
async def courses(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста, выберите предмет!", reply_markup=ikb)


@dp.callback_query_handler(text="next")
async def funct(callback: types.CallbackQuery):
    current[callback.message.chat.id] += 1

    if current[callback.message.chat.id] == len(mat_course):
        current[callback.message.chat.id] = len(mat_course) - 1

    file = InputMediaPhoto(mat_course[current[callback.message.chat.id]],
                           caption=opisanie[current[callback.message.chat.id]])

    await callback.message.edit_media(file)
    await callback.message.edit_reply_markup(reply_markup=ikbb)


@dp.callback_query_handler(text="previous")
async def funct(callback: types.CallbackQuery):
    current[callback.message.chat.id] -= 1

    if current[callback.message.chat.id] == -1:
        current[callback.message.chat.id] = 0

    file = InputMediaPhoto(mat_course[current[callback.message.chat.id]],
                           caption=opisanie[current[callback.message.chat.id]])

    await callback.message.edit_media(file)
    await callback.message.edit_reply_markup(reply_markup=ikbb)


@dp.callback_query_handler(text='menu')
async def kkk(callback: types.CallbackQuery):
    await callback.message.answer(text='hello')


@dp.callback_query_handler()
async def subjects(callback: types.CallbackQuery):
    if callback.data == 'math':
        await bot.send_photo(chat_id=callback.message.chat.id,
                             photo=str(mat_course[current[callback.message.chat.id]]),
                             caption=str(opisanie[current[callback.message.chat.id]]),
                             reply_markup=ikbb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
