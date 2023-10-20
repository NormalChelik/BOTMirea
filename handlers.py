from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

#import time
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

#Предложка
@router.callback_query(F.data == "pred")
async def start_predloshka(clbck: CallbackQuery):
    await clbck.message.edit_text("Это предложка. Сюда можно писать различные пожелания и предложения. Также тут будут появляться _мини-предложки_ для разных событий!", reply_markup=kb.predloshka)




#Доставка
@router.callback_query(F.data == "delivery")
async def delivery(clbck: CallbackQuery):
    await clbck.message.edit_text("Это раздел доставки. Выбери свою роль:", reply_markup=kb.order_menu_kb)

@router.callback_query(F.data == "courier")
async  def courier(clbck: CallbackQuery):
    orders = kb.create_order_buttons()
    await clbck.message.edit_text("Вот список всех доступных заказов (выбери заказ и нажми на него):", reply_markup=orders.as_markup())


@router.callback_query(F.data == "client")
async def client(clbck: CallbackQuery, state: FSMContext):
    if len(DataBase.check_order_client(clbck.from_user.id)) > 0:
        await clbck.message.edit_text(f"*Клиент:* @{clbck.from_user.username}\n*Ваш заказ: *'{DataBase.check_order_client(clbck.from_user.id)[0][2]}'\n\n_Вы можете отредактировать его или удалить_", reply_markup=kb.create_order_kb)

    else:
        await state.set_state(InputUserData.order_state)
        await clbck.message.edit_text("Напишите, что хотите заказать (вода, еда), цену:") 

@router.message(InputUserData.order_state)
async def input_order(message: Message, state: FSMContext):
    await state.update_data(order_state=message.text)
    DataBase.add_client_delivery(message.from_user.id, message.text, message.from_user.username)
    await message.answer(f"*Заказ добавлен!*\n\n'{DataBase.check_order_client(message.from_user.id)[0][2]}'", reply_markup=kb.create_order_kb)
    #time.sleep(3)
    #await message.edit_text(f"*Клиент:* @{message.from_user.username}\n*Ваш заказ:*'{DataBase.check_order_client(message.from_user.id)[0][2]}'\n\n_Вы можете отредактировать его или удалить_", reply_markup=kb.create_order_kb)

@router.callback_query(F.data == "edit_order")
async def edit_order(clbck: CallbackQuery, state: FSMContext):
    await state.set_state(InputUserData.order_edit_state)
    await clbck.message.edit_text("Напишите исправленный заказ и отправьте его боту:")

@router.message(InputUserData.order_edit_state)
async def input_edit_order(message: Message, state: FSMContext):
    await state.update_data(order_edit_state=message.text)
    DataBase.update_client_delivery(message.from_user.id, message.text)
    await message.answer(f"*Заказ исправлен!*\n\n'{DataBase.check_order_client(message.from_user.id)[0][2]}'", reply_markup=kb.create_order_kb)
    #time.sleep(3)
    #await message.edit_text(f"*Клиент:* @{message.from_user.username}\n*Ваш заказ:*'{DataBase.check_order_client(message.from_user.id)[0][2]}'\n\n_Вы можете отредактировать его или удалить_", reply_markup=kb.create_order_kb)

@router.callback_query(F.data == "delete_order")
async def delete_order(clbck: CallbackQuery):
    DataBase.delete_client_delivery(clbck.from_user.id)
    await clbck.answer("Вы удалили свой заказ!", show_alert=True)
    await clbck.message.edit_text("Это раздел доставки. Выбери свою роль:", reply_markup=kb.order_menu_kb)

@router.callback_query(F.data.startswith("order_call_"))
async def callback_order(clbck: CallbackQuery):
    await clbck.message.edit_text(f"*Клиент:* @{DataBase.check_order_client(clbck.data[11:])[0][3]}\n*Заказ:* {DataBase.check_order_client(clbck.data[11:])[0][2]}\n\nХотите взять заказ?", reply_markup=kb.apply_order_kb) 

@router.callback_query(F.data == "refuse_order")
async def refuse_applyorder(clbck: CallbackQuery):
    await clbck.answer("Вы отказались от заказа", show_alert=True)
    orders = kb.create_order_buttons()
    await clbck.message.edit_text("Вот список всех доступных заказов (выбери заказ и нажми на него):", reply_markup=orders.as_markup())

@router.callback_query(F.data == "back")
async def back(clbck: CallbackQuery):
    await clbck.message.edit_text("Это раздел доставки. Выбери свою роль:", reply_markup=kb.order_menu_kb)

@router.callback_query(F.data == "backmenu")
async def backmenu(clbck: CallbackQuery):
    await clbck.message.edit_text("📌                   Главное меню                  📌", reply_markup=kb.menu)

