# coder - Gmggamedev
# youtube - https://www.youtube.com/@GmgGameDev

import telebot
from telebot import types
import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users(
            id TEXT,
            name TEXT)''')

token = '7366697864:AAEDJDX6xOvjfunF-ASmwdWVKnXrRBIJkMk'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton("button")
    markup.add(button1)
    id = message.chat.id
    name = message.chat.first_name
    bot.send_photo(message.chat.id, 'https://ibb.co/TWwKkV1', f"hello {name}")
    bot.send_message(message.chat.id, f"SKIBIDI", reply_markup=markup)
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM users WHERE id = ? AND name = ?
    ''', (id, name))
    data = cur.fetchone()

    if data is None:
        try:
            cur.execute('''
            INSERT INTO users (id, name) VALUES (?, ?)
            ''', (id, name))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

@bot.message_handler(func=lambda message: True)
def buuton1_handler(message):
    chat_id = message.chat.id
    text = message.text
    if text.lower() == "button":
        bot.send_message(chat_id, "Skibidi?")
        
bot.polling(non_stop=True)
