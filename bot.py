import telebot
import env  

WELCOME_MESSAGE = "Hola, Sr."
STRANGE_PERSON_MESSAGE = "No me está permitido hablar con extraños :("
NOT_IMPLEMENTED_MESSAGE = "Sin implementar"

def known_id(id):
    return id == env.MY_CHAT_ID

bot = telebot.TeleBot(env.TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    chat_id = m.chat.id
    if known_id(chat_id):
        bot.send_message(chat_id, WELCOME_MESSAGE)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

@bot.message_handler(commands=['help'])
def help(m):
    chat_id = m.chat.id 
    if known_id(chat_id):
        bot.send_message(chat_id, NOT_IMPLEMENTED_MESSAGE)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)


bot.polling()