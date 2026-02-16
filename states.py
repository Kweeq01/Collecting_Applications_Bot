from aiogram.fsm.state import StatesGroup, State


class GetData(StatesGroup):
    name = State()
    phone_number = State()
    comment = State()