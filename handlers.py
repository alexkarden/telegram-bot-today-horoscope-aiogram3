from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards import reply_horo
from horoscript import get_horo

router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('👋 <b> Добро пожаловать! </b> \n  Выбери свой знак зодиака:', reply_markup= await reply_horo(), parse_mode=ParseMode.HTML)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Это команда /help')

@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer('<b>Alex Karden</b>\nhttps://github.com/alexkarden', parse_mode=ParseMode.HTML)

@router.message(Command('alexkarden'))
async def cmd_alexkarden(message: Message):
    await message.answer('<b>Алексей\n<a href="tel:+37529xxxxxxx">+375-29-xxx-xx-xx</a></b>', parse_mode=ParseMode.HTML)

@router.message(F.text)
async def ftext_horo(message: Message):
    await message.answer(await get_horo(message.text), parse_mode=ParseMode.HTML)


