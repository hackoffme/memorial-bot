from email.errors import MessageError
from aiogram import Dispatcher, types
from aiogram.types import Message

from tbot.kb.user_kb import markup

async def user_start(message: Message):
    await message.reply('Привет, друг. Если ты гуляешь по Волго-Донскому каналу,'\
                        'то отправив свою локацию можешь узнать'\
                        'о событиях, происходивших рядом с твоей локацией', 
                        reply_markup=markup)

async def get_location(message: Message):
    await message.answer(message)
    await message.answer(message.location)
    print(message.location.live_period)
    if message.location.live_period:
        await message.answer(f'время доступа к координатам {message.location.live_period} секунд, в'\
            'в минутах гораздо меньше')
        # Надо как  то придумать обновлять координаты
    else:
        await message.answer(f'Если в меню выбрать делиться геопозицией, то наше общение может стать'\
             'более плодотворным. Будешь получать события по всему пути своего следования')
    


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"])
    dp.register_message_handler(get_location, content_types=types.ContentTypes.LOCATION)