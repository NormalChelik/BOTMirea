from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import kb
import DataBase
from states import InputUserData

router = Router()

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
async def client(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(InputUserData.order_state)
    await clbck.message.edit_text("Напишите, что хотите заказать (вода, еда), цену:")

@router.message(InputUserData.order_state)
async def input_order(message: Message, state: FSMContext):
    await state.update_data(order_state=message.text)
    await message.answer(DataBase.add_client_delivery(message), reply_markup=kb.menu)


@router.callback_query(F.data == "backmenu")
async def back(clbck: CallbackQuery):
    await clbck.message.edit_text("📌                   Главное меню                  📌", reply_markup=kb.menu)

