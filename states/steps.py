from aiogram.dispatcher.filters.state  import StatesGroup,State


class Flow(StatesGroup):
    StartState=State()
    RegisterState=State()