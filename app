import telebot
import pyttsx3
from telebot import types

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

engine = pyttsx3.init()

@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, 'Дать полные ответы на 5 вопросов интервью. Выполнение 40 секунд на каждый ответ. Напишите "Продолжить "')
    with open('video.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, text_up)

def text_up(message):
    if message.text == 'Продолжить':
        tts_text = "Hello everybody! It's Teenagers Around the World Channel. Our guest today is a teenager from Russia and we are going to discuss teens' favourite food. We'd like to know our guest's point of view on this issue. Please answer five questions. So, let's get started."
        engine.save_to_file(tts_text, 'welcome_audio.wav')
        engine.runAndWait()
        
        with open('welcome_audio.wav', 'rb') as f:
            bot.send_audio(message.chat.id, f)
        
        msg = bot.send_message(message.chat.id, 'What is your favourite food? Why do you like it so much? Can you cookie?')
        with open('video1.mp4', 'rb') as f:
            bot.send_video(message.chat.id, f)
        bot.register_next_step_handler(msg, answer_one)
