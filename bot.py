import telebot
import env  
import time
import subprocess

#Mensajes que el bot puede enviar al usuario
WELCOME_MESSAGE = "Hola, Sr. Bienvenido de nuevo."
STRANGE_PERSON_MESSAGE = "No me está permitido hablar con extraños :("
REBOOT_MESSAGE = "Iniciando reinicio del dispositivo"
NOT_IMPLEMENTED_MESSAGE = "Sin implementar"

#Comandos de terminal que el bot puede llegar a ejecutar
reboot = ["shutdown", "-r", "now"]

bot = telebot.TeleBot(env.TOKEN)

def known_id(id):
    return id == env.MY_CHAT_ID

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

@bot.message_handler(commands=['reboot'])
def reboot_command(m):
    chat_id = m.chat.id
    if known_id(chat_id):
        print("Iniciando reinicio del dispositivo...")
        bot.send_message(chat_id, REBOOT_MESSAGE)
        time.sleep(5)
        subprocess.run(reboot)

bot.polling()