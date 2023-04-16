from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN_API = '5927151454:AAFJHukxbmwggEEiMPFXp8Pzkh5CTaLiqcE'
HELP = '''
/start - начать работу бота
/help - вывести список доступных комманд
/courses - вывести список доступных курсов
/auth - войти в свой аккаунт'''
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=4)
ib1 = InlineKeyboardButton(text='Математика🎲', callback_data='math')
ib2 = InlineKeyboardButton(text='Русский язык📔', callback_data='rus')
ib3 = InlineKeyboardButton(text='Химия🧪', callback_data='chemistry')
ib4 = InlineKeyboardButton(text='Биология🌱', callback_data='bio')
ib5 = InlineKeyboardButton(text='Физика⚙️', callback_data='phy')
ib6 = InlineKeyboardButton(text='Информатика💻', callback_data='inf')
ikb.add(ib1, ib2).add(ib3, ib4).add(ib5, ib6)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Добро пожаловать, ознакомьтесь списком возможностей коммандой "
                                "/help")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=HELP)


@dp.message_handler(commands=['courses'])
async def courses(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Пожалуйста, выберите предмет!", reply_markup=ikb)


@dp.callback_query_handler()
async def subjects(callback: types.CallbackQuery):
    await callback.message.answer(callback.data)


if __name__ == '__main__':
    executor.start_polling(dp)
