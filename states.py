from aiogram.dispatcher.filters.state import State, StatesGroup

class press(StatesGroup):
    waiting_for_click = State()