import telebot
import random
import config

chats = []
bot = telebot.TeleBot(config.token)
help_message = '''
hello world
how are you
'''
smiles = ['☺️', '😔', '🤦‍']


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, random.choice(smiles))


@bot.message_handler(commands=['stats'])
def get_statistics(message):
    bot.send_message(message.chat.id, chats)


@bot.message_handler(func=lambda message: True)
def upper(message):
    if message.chat.id not in chats:
        chats.append(message.chat.id)
    bot.reply_to(message, message.text.upper())


bot.polling()
