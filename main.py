from actions_with_currencies import *
import telebot
import config

bot = telebot.TeleBot(config.api_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Hello! This bot lets you to convert different currencies.\nEnter the currency you want to cinvert from:')
    bot.register_next_step_handler(msg, get_first_currency)

def get_first_currency(message):
    user_info = {}
    user_info['first_currency'] = message.text
    msg = bot.send_message(message.chat.id, 'Enter the currency you want to convert to')
    bot.register_next_step_handler(msg, get_second_currency, user_info)

def get_second_currency(message, user_info):
    user_info['second_currency'] = message.text
    msg = bot.send_message(message.chat.id, 'Enter the amount you want to convert')
    bot.register_next_step_handler(msg, get_amount, user_info)

def get_amount(message, user_info):
    user_info['amount'] = message.text
    bot.send_message(message.chat.id, 'Counting your results...')
    res = get_exchanged_cur(user_info['first_currency'], user_info['second_currency'], user_info['amount'])
    bot.send_message(message.chat.id, f'{user_info["first_currency"].upper()}-->{user_info["second_currency"].upper()}\nConvertion rate : {res["conversion_rate"]}\nConversion_result: {res["conversion_result"]}')

@bot.message_handler(func = lambda message: True)
def send_undefined_reply(message):
    bot.send_message(message.chat.id, 'Sorry, I didn\'t understand you')

if __name__ == '__main__':
    bot.infinity_polling()

