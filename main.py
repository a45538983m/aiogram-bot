from os import getenv
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import asyncio
from handlers.routes import router, notifier

load_dotenv()
Token = getenv("APITOKEN")

dp = Dispatcher()

dp.include_router(router)

async def main():
    bot = Bot(token=Token)
    
    asyncio.create_task(notifier(bot))
    
    print("Start...")
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main()) 