from aiogram import types, F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import kb

router = Router()

class Form(StatesGroup):
    name = State()

@router.message(Command("start"))
async def start(message: Message):
    username = message.from_user.username

    if message.from_user.username == None:
        username = "Незнакомец"

    await message.answer(f"Приветствую, *{username}*! Я МИРЭАБот с разными прикалюхами. Это главное меню.", reply_markup=kb.menu)

@router.callback_query(F.data == "delivery")
async def delivery(clbck: CallbackQuery):
    await clbck.message.edit_text("Это раздел доставки. Выбери свою роль:", reply_markup=kb.order_menu_kb)

@router.callback_query(F.data == "courier")
async  def courier(clbck: CallbackQuery):
    await clbck.message.edit_text("Вот список всех доступных заказов (выбери заказ и нажми на него):", reply_markup=kb.order.as_markup())

@router.callback_query(F.data == "client")
async def client(clbck: CallbackQuery):
    await clbck.message.edit_text("Напишите, что хотите заказать (вода, еда), цену:")



@router.callback_query(F.data == "backmenu")
async def back(clbck: CallbackQuery):
    await clbck.message.edit_text("📌                   Главное меню                  📌", reply_markup=kb.menu)

