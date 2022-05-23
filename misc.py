import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = '5336221705:AAFbkHtmbtVtwzJLhkUNMcGiUELIqxO_ewc'
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)