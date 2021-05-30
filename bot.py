import logging
from config import token
from sqlite import SQLighter
from buttons import *
from states import *
from freesteam import parse_link

from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import asyncio



logging.basicConfig(level=logging.INFO)

bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())



db = SQLighter('db.db')

# Команда активации подписки
@dp.message_handler(commands=['start'])
async def subscribe(message: types.Message):
    await message.answer("Здравствуйте, это бот для уведомлений о бесплатных играх таких как - steam, epicgames, gog, ps store и других \nВы желаете подписаться?  ", reply_markup=sub)




@dp.message_handler(state="*", text_endswith=['Отписаться', 'отписаться'])
async def stop_command(message: types.Message, state: FSMContext):
    if(not db.subscriber_exists(message.from_user.id)):
        
        db.add_subscriber(message.from_user.id, False)

        await message.answer("Вы итак не подписаны.")
    else:

        db.update_subscription(message.from_user.id, False)

        await message.answer(text="Вы отписались от рассылки", reply_markup=sub)

    await state.finish()

@dp.message_handler(Text(equals="Подписаться"))
async def subscribes(message: types.Message):
    if(not db.subscriber_exists(message.from_user.id)):

        db.add_subscriber(message.from_user.id)
    else:

        db.update_subscription(message.from_user.id, True)

    await message.answer("Вы успешно подписались на рассылку!", reply_markup=unsub)


async def scheduled(wait_for):
    link, links = parse_link()
    while 1:
        await asyncio.sleep(wait_for)

        old_link = link
        link, links = parse_link()

        subscribes = db.get_subscriptions()
        if link != old_link: # для теста можете заменить != на == 
                for s in subscribes:
                    with open("images/00000001.jpg", "rb") as photos:
                        await bot.send_photo(s[1], photo=photos, caption=f"{links} \n[*ссылка*]({link}) ", parse_mode = "MarkdownV2" )
                
                logging.info("New link")


        else:
            logging.info("sleep")



    

if __name__ == "__main__":  
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10)) # цифра 10 обозначает время отдыха
    executor.start_polling(dp, skip_updates=True)