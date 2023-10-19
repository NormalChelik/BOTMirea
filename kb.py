from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import DataBase

menu = [
    [InlineKeyboardButton(text="🛒 МИРЭАДоставка", callback_data="delivery")],
    [InlineKeyboardButton(text="📑 Предложка", callback_data="pred")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)


order_menu_kb = [
    [InlineKeyboardButton(text="📦 Курьер", callback_data="courier"), InlineKeyboardButton(text="🔔 Клиент", callback_data="client")],
    [InlineKeyboardButton(text="◀️ Назад в главное меню", callback_data="backmenu")]
]

order_menu_kb = InlineKeyboardMarkup(inline_keyboard=order_menu_kb)



create_order_kb = [
    [InlineKeyboardButton(text="✏️ Редактировать", callback_data="edit_order"), InlineKeyboardButton(text="📷 Добавить фото", callback_data="add_photo_order")],
    [InlineKeyboardButton(text="❌ Удалить", callback_data="delete_order")],
    [InlineKeyboardButton(text="◀️ Назад в главное меню", callback_data="backmenu")]
]
create_order_kb = InlineKeyboardMarkup(inline_keyboard=create_order_kb)



predloshka = [
    [InlineKeyboardButton(text="◀️ Назад в главное меню", callback_data="backmenu")],
    [InlineKeyboardButton(text="📣 Главная предложка!", callback_data="predloshka_message")],
    [InlineKeyboardButton(text="🧻 21.07.23 ПОСВЯТ!", callback_data="posvyat")]
]

predloshka = InlineKeyboardMarkup(inline_keyboard=predloshka)



def create_order_buttons():
    kb_order = DataBase.all_order_courier()

    orders = InlineKeyboardBuilder()
    orders.button(text="◀️ Назад в главное меню", callback_data="backmenu")
    for i in range(0, len(kb_order)):
        orders.button(text=f"Заказ#{i+1}: {kb_order[i][1]}", callback_data=f"order#{kb_order[i][0]}")
    orders.adjust(1)
    return orders