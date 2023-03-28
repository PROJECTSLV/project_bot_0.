import telebot
from telebot import types

# bot & API
TOKEN = '6209043627:AAFiY0KrL6IdR8e19pXuRmzHiTL-2DFRuks'

bot = telebot.TeleBot(TOKEN)
game = 'https://gabryelf.itch.io/galactic-patrulgp01'
git = 'https://github.com/PROJECTSLV/project_bot_0..git'
photo_url = 'https://cloud.mail.ru/public/Mtcn/YaHr433Ld'
@bot.message_handler(commands=['start'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Покажи план'), types.KeyboardButton('Покажи проект'))
    keyboard.add(types.KeyboardButton('Мероприятия'))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Покажи план':
        bot.send_photo(message.chat.id, photo=photo_url, caption='Это он?')
    elif message.text == 'Покажи проект':
        f = open('PSP.jpg', 'rb')
        bot.send_document(message.chat.id, document=f, caption='Это тот файл?')
    elif message.text == 'Мероприятия':
        inlineKeyboard = types.InlineKeyboardMarkup()
        inlineKeyboard.add(types.InlineKeyboardButton('1. Встречи', callback_data='Встречи'))
        inlineKeyboard.add(types.InlineKeyboardButton('2. Опросы', callback_data='Опросы'))
        inlineKeyboard.add(types.InlineKeyboardButton('3. Голосования', callback_data='Голосования'))
        bot.send_message(message.chat.id, 'Близжайшие мероприятия',reply_markup=inlineKeyboard)

@bot.callback_query_handler(func=lambda call: True)
def getAnswer(call):
    if call.data == 'Встречи':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Тут есть про это!')
    elif  call.data == 'Опросы':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Вот они!')
    elif call.data == 'Голосования':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Держите!')
    bot.answer_callback_query(call.id)

bot.polling(none_stop=True)





