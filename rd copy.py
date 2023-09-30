import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('2029315675:AAF6g4pNAcMdsF-SRh_SxNs5ATscL6pIDYM')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

# Заготовки для предложений
zvoon = '1 урок: 8.30 - 9.10 (перемена 10 минут)\n2 урок: 9.20-10.00 (перемена 20 минут)\n3 урок: 10.20 - 11.00 (перемена 20 минут)\n' \
        '4 урок: 11.10 - 12.00 (перемена 20 минут)\n5 урок: 12.20 - 13.00 (перемена 20 минут)\n6 урок: 13.20 - 14.00 (перемена 10 минут)' \
        '\n7 урок: 14.10 - 14.50'

#Список приветсвий
hello = ['Привет! Что ты хочешь посмотреть?', 'Йоу! Что ты хочешь посмотреть?', 'Шалом! Что ты хочешь посмотреть?', ' Что ты хочешь посмотреть?']


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет, я бот, я отправлю тебе расписание твоего класса. Чтобы продолжить ")
    if message.text == "Привет" or message.text == "привет":
        # Пишем приветствие
        bot.send_message(message.from_user.id, hello[random.randint(0, 3)])
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        less = types.InlineKeyboardButton(text='Расписание уроков', callback_data='rasp')
        # И добавляем кнопку на экран
        keyboard.add(less)
        zvon = types.InlineKeyboardButton(text='Расписание звонков', callback_data='raspz')
        keyboard.add(zvon)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери то, что хочешь узнать', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Чтобы начать пользоваться ботом напишите 'Привет'.\n Букву класса писать на латинице! \n Нашел баг? пиши сюда: @sulrus75")
    elif message.text == "10C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "10B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.from_user.id, open("path_to_image", 'rb'))
    elif message.text == "10E":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "10A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "11A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "11B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "11C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "11E":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "6A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "6B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "6C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "7A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "7B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "7C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "7M":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "8A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "8B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "8C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "8D":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "9A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "9B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "9C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "9D":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    elif message.text == "9M":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open("path_to_image", 'rb'))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "raspz":
        msg = zvoon
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'rasp':
        msg = 'Напиши свой клас, буква с большой буквы, на латинице! Например: 10С'
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
