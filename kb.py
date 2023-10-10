from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb_order = [1, 2, 3, 4,
            5, 6, 7, 8,
            9, 10, 11, 12,
            13, 14
            ]
menu = [
    [InlineKeyboardButton(text="МИРЭАДоставка", callback_data="delivery")]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)

order_menu_kb = [
    [InlineKeyboardButton(text="📦 Курьер", callback_data="courier"), InlineKeyboardButton(text="🔔 Клиент", callback_data="client")],
    [InlineKeyboardButton(text="◀️ Назад в главное меню", callback_data="backmenu")]
]

order_menu_kb = InlineKeyboardMarkup(inline_keyboard=order_menu_kb)

order = InlineKeyboardBuilder()
order.button(text="◀️ Назад в главное меню", callback_data="backmenu")
for i in range(0, len(kb_order)):
    order.button(text=f"Заказ#{kb_order[i]}", callback_data=f"order#{kb_order[i]}")
order.adjust(1)