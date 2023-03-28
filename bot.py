import time
import logging
import telebot
from telebot import types

from aiogram import Bot, Dispatcher, executor, types


# bot & API
TOKEN = '6209043627:AAFiY0KrL6IdR8e19pXuRmzHiTL-2DFRuks'
MSG = "Даешь код!!! {}"

bot = telebot.TeleBot(TOKEN)
game = 'https://gabryelf.itch.io/galactic-patrulgp01'
git = 'https://github.com/PROJECTSLV/project_bot_0..git'
#dp = Dispatcher(bot)


#@dp.message_handler(commands=['start'])
# возвращает тоже что ему сообщили.
#async def echo(message: types.Message):
    #await message.answer(text=message.text)


async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id=} {user_full_name=} {time.asctime()}')
    await message.reply(f"Привет, {user_name}!")

    for i in range(10):
        time.sleep(2)
        await bot.send_message(user_id, MSG.format(user_name))
@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Зарубать!'), types.KeyboardButton('Слиться...'))
    bot.send_message(message.chat.id, f'Привет )) {message.from_user.first_name}!', reply_markup=keyboard)

@bot.message_handler(conteint_types=['text'])
def main_menu(message):
    if message.text == 'Зарубать!':
        bot.send_message(message.chat.id, inline_message_id=game)
    elif message.text == 'Слиться...!':
        bot.send_message(message.chat.id, inline_message_id=git)

bot.polling(none_stop=True)


#if __name__ == '__main__':
#    executor.start_polling(bot)


