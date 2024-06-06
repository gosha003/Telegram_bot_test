from telebot import types
import telebot

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):

    chat_id = message.chat.id
    print(f"send_welcome message: {message}")
    print(f"echo_all message: {message}")
    print(f"chat_id: {chat_id}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("Hello!")
    btn2 = types.KeyboardButton('How are you?')
    btn3 = types.KeyboardButton("Goodbye!")
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "Hello, I'm your bot!", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_and_respond_to_messages (message):

    chat_id = message.chat.id
    if message.text == "Hello!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Wow!")
        markup.add(btn1)
        bot.send_message(chat_id, "Hello, my name is bot! Select your next response", reply_markup = markup)

    elif message.text == "How are you?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Wow!")
        markup.add(btn1)
        bot.send_message(chat_id, "I'm doing great, thanks! Select your next response", reply_markup = markup)

    elif message.text == "Goodbye!":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Wow!")
        markup.add(btn1)
        bot.send_message(chat_id, "Alright, goodbye! Select your next response", reply_markup = markup)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#
#     bot.reply_to(message, message.text)


# def write_smth():
#
#     chat_id = 954242166
#     bot.send_message(chat_id, "Hey!")


# write_smth()
bot.polling(none_stop=True, interval=0)