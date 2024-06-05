from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Filter, CommandStart, Command

admin = Router()


class Admin(Filter):
    def __init__(self):
        self.admins = [123, 456]

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins
    

@admin.message(Admin(), Command('admin'))
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в бот, администратор!')
