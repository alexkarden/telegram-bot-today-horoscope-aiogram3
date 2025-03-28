from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_horo = ['♈️ Овен','♉️ Телец','♊️ Близнецы','♋️ Рак','♌️ Лев','♍️ Дева','♎️ Весы','♏️ Скорпион','♐️ Стрелец','♑️ Козерог','♒️ Водолей','♓️ Рыбы']

async def reply_horo():
    keyboard =ReplyKeyboardBuilder()
    for horo in keyboard_horo:
        keyboard.add(KeyboardButton(text = horo))
    return keyboard.adjust(3).as_markup(resize_keyboard=True)