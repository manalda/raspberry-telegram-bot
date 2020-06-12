import telebot
import env  
import time
import subprocess

#Diccionario con todos los comandos que puede aceptar el bot
available_commands = {"start":"inicia una conversacion con el bot",
"reboot":"reinicia el equipo", "halt":"apaga el equipo", 
"help":"muestra los comandos disponibles", "tomcat":"inicia el servidor web tomcat"}

#Mensajes que el bot puede enviar al usuario
WELCOME_MESSAGE = "Hola, Sr. Bienvenido de nuevo."
STRANGE_PERSON_MESSAGE = "No me está permitido hablar con extraños :("
REBOOT_MESSAGE = "Iniciando reinicio del dispositivo"
HALT_MESSAGE = "Iniciando apagado del dispositivo"
HELP_MESSAGE = "Lista de comandos disponibles:\n"
NOT_IMPLEMENTED_MESSAGE = "Sin implementar"
UNKNOWN_COMMAND_MESSAGE = "No entiendo el mensaje :("
for c in available_commands.keys():
    HELP_MESSAGE += ("\t" + "/" + c + " - " + available_commands[c] + "\n") 

#Comandos de terminal que el bot puede llegar a ejecutar
reboot = ["shutdown", "-r", "now"]
halt = ["shutdown", "-h", "now"]

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
        bot.send_message(chat_id, HELP_MESSAGE)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

@bot.message_handler(commands=['reboot'])
def reboot_command(m):
    chat_id = m.chat.id
    if known_id(chat_id):
        bot.send_message(chat_id, REBOOT_MESSAGE)
        time.sleep(5)
        subprocess.run(reboot)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

@bot.message_handler(commands=['halt'])
def halt_command(m):
    chat_id = m.chat.id 
    if known_id(chat_id):
        bot.send_message(chat_id, HALT_MESSAGE)
        time.sleep(5)
        subprocess.run(halt)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

@bot.message_handler(commands=['tomcat'])
def tomcat(m):
    chat_id = m.chat.id
    if known_id(chat_id):
        bot.send_message(chat_id, NOT_IMPLEMENTED_MESSAGE)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

@bot.message_handler(func=lambda m: True, content_types=['text'])
def unknown_message(m):
    chat_id = m.chat.id
    if known_id(chat_id):
        bot.send_message(chat_id, UNKNOWN_COMMAND_MESSAGE)
    else:
        bot.send_message(chat_id, STRANGE_PERSON_MESSAGE)

bot.polling()