from aiogram.fsm.state import StatesGroup, State


class InputUserData(StatesGroup):
    order_state = State()
    order_edit_state = State()
