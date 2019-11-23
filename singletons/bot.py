from aiogram import Dispatcher
from aiogram.bot import Bot as TelegramBot

from utils.singleton import singleton


@singleton
class Bot(TelegramBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dispatcher = Dispatcher(self)
