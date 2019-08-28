import telebot
from telebot.types import Message
import random

TOKEN = '661578501:AAGvskDr0zwqxOGbqeOCCYWnMxMcnYMu3tE'
bot = telebot.TeleBot(TOKEN)
help_message = '''
hello world
how are you
'''

smiles = ['☺️', '😔', '🤦‍' ]
@bot.message_handler(commands = ['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, random.choice(smiles))

@bot.message_handler(func = lambda message: True)
def upper(message: Message):
    bot.reply_to(message, message.text.upper())

bot.polling()