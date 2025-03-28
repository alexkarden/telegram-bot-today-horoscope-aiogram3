import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router


bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')