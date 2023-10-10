from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

import kb

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    username = message.from_user.username

    if message.from_user.username == None:
        username = "Незнакомец"

    await message.answer(f"Приветствую, *{username}*! Выбери свою роль.", reply_markup=kb.menu)

@router.callback_query(F.data == "courier")
async  def courier(clbck: CallbackQuery):
    await clbck.message.edit_text("Выбери заказ:", reply_markup=kb.order)