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
    await clbck.message.edit_text("Вот список всех доступных заказов (выбери заказ и нажми на него):", reply_markup=kb.orders.as_markup())


@router.callback_query(F.data == "client")
async def client(clbck: CallbackQuery, state: FSMContext):
    if len(DataBase.check_order_client(clbck.from_user.id)) > 0:
        await clbck.message.edit_text(f"*Ваш заказ:* '{DataBase.check_order_client(clbck.from_user.id)[0][2]}' вы можете отредактировать или удалить", reply_markup=kb.create_order_kb)

    else:
        await state.set_state(InputUserData.order_state)
        await clbck.message.edit_text("Напишите, что хотите заказать (вода, еда), цену:") 

@router.message(InputUserData.order_state)
async def input_order(message: Message, state: FSMContext):
    await state.update_data(order_state=message.text)
    DataBase.add_client_delivery(message.from_user.id, message.text)
    await message.answer(f"*Заказ* '{DataBase.check_order_client(message.from_user.id)[0][2]}' *добавлен*!", reply_markup=kb.create_order_kb)

@router.callback_query(F.data == "edit_order")
async def edit_order(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(InputUserData.order_edit_state)
    await clbck.message.edit_text("Напишите исправленный заказ и отправьте его боту:")

@router.message(InputUserData.order_edit_state)
async def input_edit_order(message: Message, state: FSMContext):
    await state.update_data(order_edit_state=message.text)
    DataBase.edit_client_delivery(message.from_user.id, message.text)
    await message.answer(f"*Заказ* '{DataBase.check_order_client(message.from_user.id)[0][2]}' *исправлен*!", reply_markup=kb.create_order_kb)

@router.callback_query(F.data == "backmenu")
async def back(clbck: CallbackQuery):
    await clbck.message.edit_text("📌                   Главное меню                  📌", reply_markup=kb.menu)

