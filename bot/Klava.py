from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb = InlineKeyboardMarkup(row_width=4)
ib1 = InlineKeyboardButton(text='Математика🎲', callback_data='math')
ib2 = InlineKeyboardButton(text='Русский язык📔', callback_data='rus')
ib3 = InlineKeyboardButton(text='Химия🧪', callback_data='chemistry')
ib4 = InlineKeyboardButton(text='Биология🌱', callback_data='bio')
ib5 = InlineKeyboardButton(text='Физика⚙️', callback_data='phy')
ib6 = InlineKeyboardButton(text='Информатика💻', callback_data='inf')
ikb.add(ib1, ib2).add(ib3, ib4).add(ib5, ib6)

ikbb = InlineKeyboardMarkup(row_width=4)
ibb1 = InlineKeyboardButton(text='Следующий курс ->', callback_data='next')
ibb2 = InlineKeyboardButton(text='<- Предыдущий курс', callback_data='previous')
ibb3 = InlineKeyboardButton(text='Перейти к выбору предмета', callback_data='menu')
ibb4 = InlineKeyboardButton(text='Оплатить курс', callback_data='payment')
ikbb.add(ibb2, ibb1)
ikbb.add(ibb3, ibb4)
