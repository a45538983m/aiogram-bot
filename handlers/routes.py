from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram import Bot 
import asyncio
router = Router()

subscribers = set()

async def notifier(bot: Bot):
    while True:
        if subscribers:
            for user_id in list(subscribers):
                try:
                    await bot.send_message(user_id,"Ваше стандартное сообщеные")
                except Exception:
                    pass

        await asyncio.sleep(10)
        
@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет!\n"
                         "Я могу помочь с рассылкой!\n\n"
                         "Команды: \n"
                         "/subscribe - подписаться на уведомленыя \n"
                         "/unsubscribe - отписаться \n"
                         "/subscribers - список подписчиков"
                         )

@router.message(Command("subscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id
    
    subscribers.add(user_id)
    
    await message.answer("Вы подписаны!")
    
@router.message(Command("unsubscribe"))
async def subscribe(message: Message):
    user_id = message.from_user.id
    
    subscribers.discard(user_id)
    
    await message.answer("Вы отписаны!")
        
    
@router.message(Command("subscribers"))
async def subscribers_cmd(message: Message):
    if not subscribers:
        await message.answer("Пока никого нет")
    
    
    text = "Подписчики:\n"
    for uid in subscribers:
        text += f"{uid}\n"
    await message.answer(text)
    