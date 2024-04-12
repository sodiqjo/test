import telebot
import requests
from telebot import types

token = '7025373255:AAHFez-z5JPQPztT5RkUYMC0eWddhxspPa0'

API = ""

bot = telebot.Telebot(token)


@bot.message_handler(commands=['start'])
def start(message):
    user_info = get_info(message)
    store_user_data(message.chat.id, user_info)
    markup=types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('GBP', callback_data='GBP'),
               types.InlineKeyboardButton('USD', callback_data='USD'),
               types.InlineKeyboardButton('RUB', callback_data='RUB'))
    bot.send_message(message.chat.id, "Choose a currency:", reply_markup = markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    querystring={"from": call.data, "to": "UZS", "amount": "1"}
    headers = {
        "X-RapidAPI-Key": "b532372ffbmsh050c418ead3d5a6p16a6a9jsnb6a2bf1688d1",
        "X-RapidAPI-Host": "currency-converter-pro1.p.rapidapi.com"
    }
    # response = requests.get(API, headers-headers, params-querystring)
    response = requests.get(my_url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        conversion_result = data['result']
        bot.send_message(call.message.chat.id, f'Conversion result: {conversion_result}')
        bot.send_message(call.message.chat.id, f'Your info: {user_data}')
    else:
        bot.send_message(call.message.chat.id, 'Failed to perform conversion. Please try again later.')
# user_list = list(user_data)
print("The bot is running...")
conn.commit()
cur.close()
conn.close()
bot.polling(none_stop=True)
