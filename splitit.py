import logging

import aiogram

from singletons.bot import Bot
from singletons.config import Config


def main():
    logging.basicConfig(level=logging.DEBUG if Config()["DEBUG"] else logging.INFO)
    Bot(Config()["TELEGRAM_API_TOKEN"])
    from bot import start
    from bot import splitit
    aiogram.executor.start_polling(Bot().dispatcher, skip_updates=True)


if __name__ == '__main__':
    main()
