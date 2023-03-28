import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

import api
import core
from api import *

bot = telebot.TeleBot(get_api())


# Приветственное сообщение при запуске бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать!\n' + str(message.chat.id))
    core.add_contact(str(message.chat.id))


# создание рассылки (при наличии прав администратора)
@bot.message_handler(commands=['send'])
def mailing_messages(message):
    if str(message.chat.id) == api.admin():
        msg = bot.reply_to(message, """\
    Введите сообщение для рассылки:
    """)
        bot.register_next_step_handler(msg, snd_msg)
    else:
        bot.reply_to(message, """\
            Вы не можете пользоваться этой командой! т.к. не являетесь администратором.
            """)


def snd_msg(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, send_mail(message.text), disable_notification=False)


def send_mail(msg):
    for id_user in core.array():
        if id_user != '\n' or id_user != ' ':
            bot.send_message(id_user, msg, disable_notification=False)
    return 'Все сообщения разосланы'


id_user_to_ans = None


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if str(message.chat.id) != api.admin():
        bot.send_message(int(api.admin()), "Вам новое сообщение от:" + message.from_user.first_name
                         + "\n" + message.text, reply_markup=gen_markup())
        id_user_to_ans = message.chat.id
        bot.reply_to(message, "Отправил ваше сообщение!")


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Ответить", callback_data="cb_yes"))
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        # bot.send_message(api.admin(), 'Введите ваш ответ в следующем сообщении')
        msg = bot.reply_to(call, 'How old are you?')
        bot.register_next_step_handler(msg, answers)


@bot.message_handler(func=lambda message: True)
def answers(message):
    bot.send_message(id_user_to_ans, message.text)

print('бот запущен!')
bot.infinity_polling()
