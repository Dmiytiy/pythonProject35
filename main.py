import telebot
from telebot import types

bot = telebot.TeleBot('6092495489:AAG_Y7gwVCcgm2tz_WUg0-Ud1xwX52XWFy0')



@bot.message_handler(commands=['start'])
def start(message):

    msg = bot.send_message(message.chat.id, 'Дать полные ответы на 5 вопросов интервью. '
                                            'Выполнение 40 секунд на каждый ответ. Напишите "Продолжить "')
    with open('video.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, text_up)


def text_up(message):

    if message.text == 'Продолжить':
        msg = bot.send_message(message.chat.id, 'Текст:\n\n'
                                      'Task 3. You are going to give an interview. You have to answer five questions.'
                                      'Give full answers to the questions (2-3 sentences).'
                                      'Remember that you have 40 seconds to answer each question. Напишите Продолжить')

    # Отправляем видео после приветственного сообщения
        with open('video1.mp4', 'rb') as f:
            bot.send_video(message.chat.id, f)
        bot.register_next_step_handler(msg, audio)

#@bot.message_handler(func=lambda message: True)
def audio(message):
    msg = bot.send_message(message.chat.id, 'Аудио:\n\n'
                                      "Hello everybody! It's Teenagers Around the World Channel."
                                      "Our guest today is a teenager from Russia and we are going to discuss teens"
                                      "favourite food. We'd like to know our guest's point of view on this issue."
                                      "Please answer five questions. So, let's get started.")
    msg = bot.send_message(message.chat.id, "Аудио:"
                                      "What is your favourite food? Why do you like it so much? Can you"
                                      "cookie?")
    # Отправляем видео после приветственного сообщения
    with open('video2.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, answer_one)

def answer_one(message):
    msg = bot.send_message(message.chat.id, "Аудио:"
                                            "Have your food preferences changed over time? Why or why not?")
    with open('video2.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, answer_two)

def answer_two(message):
    msg = bot.send_message(message.chat.id, "Аудио:"
                                            "Do you think your favourite food is healthy? Is there any unhealthy food that you like?")
    with open('video2.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, answer_three)

def answer_three(message):
    msg = bot.send_message(message.chat.id, "Аудио:"
                                            "How often do you eat your favourite food? Would you like to eat it more often?")
    with open('video2.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, answer_four)
def answer_four(message):
    msg = bot.send_message(message.chat.id, "Аудио:"
                                            "Thank you very much for your interview")
    with open('video2.mp4', 'rb') as f:
        bot.send_video(message.chat.id, f)
    bot.register_next_step_handler(msg, answer_four)

bot.polling(none_stop=True)#Постоянно выполняется