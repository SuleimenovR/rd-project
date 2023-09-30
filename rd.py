import os
import random
# Подключаем модуль для Телеграма
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Указываем токен
bot = telebot.TeleBot('2029315675:AAF6g4pNAcMdsF-SRh_SxNs5ATscL6pIDYM')
current_file = os.path.realpath(__file__)
current_directory = os.path.dirname(current_file) + '\\3.jpg'


# Заготовки для предложений
zvoon = '1 урок: 8:30 - 9:10 (перемена 10 минут)\n2 урок: 9:20 - 10:00 (перемена 20 минут)\n' \
        '3 урок: 10:20 - 11:00 (перемена 20 минут)\n' \
        '4 урок: 11:10 - 12:00 (перемена 20 минут)\n5 урок: 12:20 - 13:00 (перемена 20 минут)\n' \
        '6 урок: 13:20 - 14:00 (перемена 10 минут)' \
        '\n7 урок: 14:10 - 14:50'
hello = ['Привет! Что ты хочешь посмотреть?', 'Шалом! Что ты хочешь посмотреть?', ' Что ты хочешь посмотреть?']


# Список приветсвий
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Напишите /menu, чтобы вернуться в меню.\n'
                                      'Список команд /commands\n'
                                      'Нашел баг? Пиши сюда @username')


@bot.message_handler(commands=['commands'])
def commands_message(message):
    bot.send_message(message.chat.id, 'Список комманд:\n /start - запуск бота\n/menu - меню\n/help - помощь\n'
                                      '/commands - список комманд\n')


@bot.message_handler(commands=['physics'])
def physics_message(message):
    keyboard = types.InlineKeyboardMarkup()
    kon = types.InlineKeyboardButton(text='Храмова Ольга Николаевна', callback_data='kon')
    keyboard.add(kon)
    tnv = types.InlineKeyboardButton(text='Тележников Никита Вадимович', callback_data='tnv')
    keyboard.add(tnv)
    mri = types.InlineKeyboardButton(text='Мубаракшин Рафис Исламович', callback_data='mri')
    keyboard.add(mri)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['math'])
def math_message(message):
    keyboard = types.InlineKeyboardMarkup()
    svi = types.InlineKeyboardButton(text='Сухарев Владимир Игоревич', callback_data='svi')
    keyboard.add(svi)
    bds = types.InlineKeyboardButton(text='Бисеров Денис Сергеевич', callback_data='bds')
    keyboard.add(bds)
    vai = types.InlineKeyboardButton(text='Володина Алена Игоревна', callback_data='vai')
    keyboard.add(vai)
    dos = types.InlineKeyboardButton(text='Дунаева Ольга Сергеевна', callback_data='dos')
    keyboard.add(dos)
    kaa = types.InlineKeyboardButton(text='Хуснуллина Альбина Альбертовна', callback_data='kaa')
    keyboard.add(kaa)
    kaa2 = types.InlineKeyboardButton(text='Калимуллина Алия Айдаровна', callback_data='kaa2')
    keyboard.add(kaa2)
    pea = types.InlineKeyboardButton(text='Парышева Евгения Анатольевна', callback_data='pea')
    keyboard.add(pea)
    soa = types.InlineKeyboardButton(text='Шайдуллина Ольга Александровна', callback_data='soa')
    keyboard.add(soa)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['informatics'])
def informatics_message(message):
    keyboard = types.InlineKeyboardMarkup()
    bpg = types.InlineKeyboardButton(text='Бергер Полина Григорьевна', callback_data='bpg')
    keyboard.add(bpg)
    ksr = types.InlineKeyboardButton(text='Кутлимуратов Санжар Рустамович', callback_data='ksr')
    keyboard.add(ksr)
    meb = types.InlineKeyboardButton(text='Машанина Елена Борисовна', callback_data='meb')
    keyboard.add(meb)
    msi = types.InlineKeyboardButton(text='Михайлин Сергей Иванович', callback_data='msi')
    keyboard.add(msi)
    hbr = types.InlineKeyboardButton(text='Хисматов Булат Рафикович', callback_data='hbr')
    keyboard.add(hbr)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['project'])
def project_message(message):
    keyboard = types.InlineKeyboardMarkup()
    gat = types.InlineKeyboardButton(text='Гараева Алия Талгатовна', callback_data='gat')
    keyboard.add(gat)
    ksr = types.InlineKeyboardButton(text='Кутлимуратов Санжар Рустамович', callback_data='ksr')
    keyboard.add(ksr)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['chemistry'])
def chemistry_message(message):
    keyboard = types.InlineKeyboardMarkup()
    ron = types.InlineKeyboardButton(text='Романова Ольга Николаевна', callback_data='ron')
    keyboard.add(ron)
    tnv2 = types.InlineKeyboardButton(text='Трошанин Никита Владиславович', callback_data='tnv2')
    keyboard.add(tnv2)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['english'])
def english_message(message):
    keyboard = types.InlineKeyboardMarkup()
    iau = types.InlineKeyboardButton(text='Имамеева Алина Юнусовна', callback_data='iau')
    keyboard.add(iau)
    kak = types.InlineKeyboardButton(text='Кибякова Аида Климентовна', callback_data='kak')
    keyboard.add(kak)
    rga = types.InlineKeyboardButton(text='Рохас Гузель Альфредовна', callback_data='rga')
    keyboard.add(rga)
    uar = types.InlineKeyboardButton(text='Усманова Алла Рифатовна', callback_data='uar')
    keyboard.add(uar)
    sea = types.InlineKeyboardButton(text='Шакурова Елена Анатольевна', callback_data='sea')
    keyboard.add(sea)
    smn = types.InlineKeyboardButton(text='Швейкина Марина Николаевна', callback_data='smn')
    keyboard.add(smn)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['depdirectors'])
def depdirectors_message(message):
    keyboard = types.InlineKeyboardMarkup()
    drm = types.InlineKeyboardButton(text='Даминова Раиса Махмуриевна', callback_data='drm')
    keyboard.add(drm)
    meb = types.InlineKeyboardButton(text='Машанина Елена Борисовна', callback_data='meb')
    keyboard.add(meb)
    roo = types.InlineKeyboardButton(text='Романенко Олег Олегович', callback_data='roo')
    keyboard.add(roo)
    srf = types.InlineKeyboardButton(text='Самерханова Резида Фаатовна', callback_data='srf')
    keyboard.add(srf)
    kaa3 = types.InlineKeyboardButton(text='Хавкина Ирина Александровна', callback_data='kaa3')
    keyboard.add(kaa3)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['french'])
def french_message(message):
    keyboard = types.InlineKeyboardMarkup()
    mgr = types.InlineKeyboardButton(text='Миннигалеева Гульфия Рустемовна', callback_data='mgr')
    keyboard.add(mgr)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['biology'])
def biology_message(message):
    keyboard = types.InlineKeyboardMarkup()
    vsd = types.InlineKeyboardButton(text='Ветлужских Сергей Дмитриевич', callback_data='vsd')
    keyboard.add(vsd)
    vni = types.InlineKeyboardButton(text='Сафиуллина Наталья Ивановна', callback_data='vni')
    keyboard.add(vni)
    sgu = types.InlineKeyboardButton(text='Сибгатуллина Гульназ Юнусовна', callback_data='sgu')
    keyboard.add(sgu)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['geography'])
def geography_message(message):
    keyboard = types.InlineKeyboardMarkup()
    gat = types.InlineKeyboardButton(text='Гараева Алия Талгатовна', callback_data='gat')
    keyboard.add(gat)
    sgu = types.InlineKeyboardButton(text='Сибгатуллина Гульназ Юнусовна', callback_data='sgu')
    keyboard.add(sgu)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['history'])
def history_message(message):
    keyboard = types.InlineKeyboardMarkup()
    bds2 = types.InlineKeyboardButton(text='Билалова Дина Султановна', callback_data='bds2')
    keyboard.add(bds2)
    ean = types.InlineKeyboardButton(text='Егорова Алевтина Николаевна', callback_data='ean')
    keyboard.add(ean)
    yae = types.InlineKeyboardButton(text='Яковлев Александр Евгеньевич', callback_data='yae')
    keyboard.add(yae)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['director'])
def director_message(message):
    bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    bot.send_message(message.from_user.id, "Скобельцына Елена Германовна\nНомер кабинета: 111\n"
                                           "E-mail: EGSkobelcyna@kpfu.ru")


@bot.message_handler(commands=['music'])
def music_message(message):
    keyboard = types.InlineKeyboardMarkup()
    gga = types.InlineKeyboardButton(text='Гимаева Гузель Анваровна', callback_data='gga')
    keyboard.add(gga)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['russian'])
def russian_message(message):
    keyboard = types.InlineKeyboardMarkup()
    gnu = types.InlineKeyboardButton(text='Гатаулина Наталья Уркеновна', callback_data='gnu')
    keyboard.add(gnu)
    lov = types.InlineKeyboardButton(text='Лапина Ольга Викторовна', callback_data='lov')
    keyboard.add(lov)
    maf = types.InlineKeyboardButton(text='Муравьев Александр Федорович', callback_data='maf')
    keyboard.add(maf)
    pta = types.InlineKeyboardButton(text='Петухова Татьяна Анатольевна', callback_data='pta')
    keyboard.add(pta)
    kgd = types.InlineKeyboardButton(text='Хусаенова Гузель Динаровна', callback_data='kgd')
    keyboard.add(kgd)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['nl'])
def nl_message(message):
    keyboard = types.InlineKeyboardMarkup()
    ggf = types.InlineKeyboardButton(text='Гагарина Гульнур Фатрахмановна', callback_data='ggf')
    keyboard.add(ggf)
    iau = types.InlineKeyboardButton(text='Имамеева Алина Юнусовна', callback_data='iau')
    keyboard.add(iau)
    mdm = types.InlineKeyboardButton(text='Малмыгина Долорес Махмуриевна', callback_data='mdm')
    keyboard.add(mdm)
    mfm = types.InlineKeyboardButton(text='Мухаметшин Фанис Мухаметгалиевич', callback_data='mfm')
    keyboard.add(mfm)
    tfa = types.InlineKeyboardButton(text='Тазиева Флюра Ахтамовна', callback_data='tfa')
    keyboard.add(tfa)
    kgf = types.InlineKeyboardButton(text='Харисова Гульназ Фаритовна', callback_data='kgf')
    keyboard.add(kgf)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


@bot.message_handler(commands=['pe'])
def pe_message(message):
    keyboard = types.InlineKeyboardMarkup()
    zov = types.InlineKeyboardButton(text='Залялиева Ольга Владимировна', callback_data='zov')
    keyboard.add(zov)
    kvr = types.InlineKeyboardButton(text='Кашафутдинов Владислав Ренартович', callback_data='kvr')
    keyboard.add(kvr)
    roo = types.InlineKeyboardButton(text='Романенко Олег Олегович', callback_data='roo')
    keyboard.add(roo)
    bot.send_message(message.from_user.id, text='Выбери учителя:', reply_markup=keyboard)


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет" or message.text == "привет" or message.text == "/start":
        # Пишем приветствие
        # bot.send_message(message.from_user.id, hello[random.randint(0, 2)])
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждой кнопки
        less = types.InlineKeyboardButton(text='Расписание уроков', callback_data='rasp')
        # И добавляем кнопку на экран
        keyboard.add(less)
        zvon = types.InlineKeyboardButton(text='Расписание звонков', callback_data='raspz')
        keyboard.add(zvon)
        teachers = types.InlineKeyboardButton(text='Наши учителя', callback_data='teachers')
        keyboard.add(teachers)
        con = types.InlineKeyboardButton(text='Контакты', callback_data='con')
        keyboard.add(con)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, hello[random.randint(0, 2)], reply_markup=keyboard)
    elif message.text == "/menu" or message.text == "меню" or message.text == "Меню":
        # Пишем приветствие
        # bot.send_message(message.from_user.id, hello[random.randint(0, 2)])
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждой кнопки
        less = types.InlineKeyboardButton(text='Расписание уроков', callback_data='rasp')
        # И добавляем кнопку на экран
        keyboard.add(less)
        zvon = types.InlineKeyboardButton(text='Расписание звонков', callback_data='raspz')
        keyboard.add(zvon)
        teachers = types.InlineKeyboardButton(text='Наши учителя', callback_data='teachers')
        keyboard.add(teachers)
        con = types.InlineKeyboardButton(text='Контакты', callback_data='con')
        keyboard.add(con)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Выбери:', reply_markup=keyboard)
    # elif message.text == "/help":
    #     bot.send_message(message.from_user.id, "Напишите '/start', чтобы начать пользоваться ботом.\n"
    #                                            " Букву класса писать на латинице! \n Нашел баг? пиши сюда: @sulrus75")
    elif message.text == "10C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "10B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.from_user.id, open(current_directory, 'rb'))
    elif message.text == "10E":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "10A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "11A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "11B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "11C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "11E":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "6A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "6B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "6C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "7A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "7B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "7C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "7M":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "8A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "8B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "8C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "8D":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "9A":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "9B":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "9C":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "9D":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    elif message.text == "9M":
        bot.send_message(message.from_user.id, "Фото грузится")
        bot.send_photo(message.chat.id, open(current_directory, 'rb'))
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.\n"
                                               "Чтобы увидеть список команд пропишите /commands")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "raspz":
        msg = zvoon
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'rasp':
        msg = 'Напиши свой класс с большой буквы на латинице! Например: 10С'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'con':
        msg = 'Сайты лицея: http://liceum.kpfu.ru;  http://edu.tatar.ru/vahit/kpfu\n' \
              'Адрес электронной почты: liceum.kpfu@inbox.ru\n' \
              'Официальная группа лицея в ВКонтакте: https://vk.com/lobachevskylyceum\n' \
              'Официальный канал лицея в Telegram: https://t.me/lkpfu'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'teachers':
        msg = 'Выбери предмет учителя\n /director - Директор Лицея\n /depdirectors - Заместители директора\n ' \
              '/english - Английский язык\n ' \
              '/biology - Биология\n /geography - География\n' \
              ' /informatics - Информатика и ИКТ\n /history - История и обществозание\n /math - Математика\n ' \
              '/music - Музыка\n' \
              ' /obj - ОБЖ\n /russian - Русский язык и литература\n /nl - Родной язык и родная литература\n ' \
              '/project - Технология\n' \
              ' /physics - Физика\n /pe - Физическая культура\n /french - Французский язык\n' \
              ' /chemistry - Химия'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kon':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Храмова Ольга Николаевна\nНомер кабинета: 207'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'tnv':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Тележников Никита Вадимович\nНомер кабинета: 210\nВконтакте: https://vk.com/nkitik'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'mri':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Мубаракшин Рафис Исламович\nНомер кабинета: 211\nE-mail: RaIMubarakshin@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'bds':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Бисеров Денис Сергеевич\nНомер кабинета: 308'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'vai':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Володина Алена Игоревна\nНомер кабинета: 311\nE-mail: AlIVolodina@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'dos':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Дунаева Ольга Сергеевна\nНомер кабинета: 205'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kaa':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Хуснуллина Альбина Альбертовна\nНомер кабинета: 103\nE-mail: Albinana@bk.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kaa2':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Калимуллина Алия Айдаровна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'pea':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Парышева Евгения Анатольевна\nНомер кабинета: 312'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'bpg':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Бергер Полина Григорьевна\nНомер кабинета: 202'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'ksr':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Кутлимуратов Санжар Рустамович\nНомер кабинета: 105\nE-mail: sanjar.kr@gmail.com'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'meb':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Машанина Елена Борисовна\nЗаместитель директора по учебной работе\nE-mail: EBMashanina@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'msi':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Михайлин Сергей Иванович\nНомер кабинета: 220\nE-mail: sergm55@mail.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'hbr':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Хисматов Булат Рафикович\nНомер кабинета: 120\nE-mail: bulatrh2015@yandex.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'svi':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Сухарев Владимир Игоревич'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'soa':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Шайдуллина Ольга Александровна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'gat':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Гараева Алия Талгатовна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'tnv2':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Трошанин Никита Владиславович\nНомер кабинета: 309\nE-mail: NiVTroshanin@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'ron':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Романова Ольга Николаевна\nНомер кабинета: 309\nE-mail: olga755954@mail.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'mgr':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Миннигалеева Гульфия Рустемовна\nE-mail: gulfiarustemovna@mail.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'iau':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Имамеева Алина Юнусовна\nE-mail: AlJSadykova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kak':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Кибякова Аида Климентовна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'rga':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Рохас Гузель Альфредовна\nНомер кабинета: 312'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'uar':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Усманова Алла Рифатовна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'sea':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Шакурова Елена Анатольевна\nНомер кабинета: 326'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'smn':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Швейкина Марина Николаевна\nНомер кабинета: 204\nE-mail: MNShvejkina@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'vsd':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Ветлужских Сергей Дмитриевич'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'vni':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Сафиуллина Наталья Ивановна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'sgu':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Cибгатуллина Гульназ Юнусовна\nНомер кабинета: 227'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'bds2':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Билалова Дина Султановна\nE-mail: DSBilalova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'ean':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Егорова Алевтина Николаевна\nНомер кабинета: 203'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'yae':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Яковлев Александр Евгеньевич\nНомер кабинета: 218'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'gga':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Гимаева Гузель Анваровна\nНомер кабинета: 303\nE-mail: Guzel.Gimaeva@ksu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kvu':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Клинцов Виктор Юрьевич\nНомер кабинета: 219\nE-mail: VJKlincov@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'gnu':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Гатаулина Наталья Уркеновна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'lov':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Лапина Ольга Викторовна\nНомер кабинета: 320'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'maf':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Муравьев Александр Федорович\nНомер кабинета: 307'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'pta':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Петухова Татьяна Анатольевна'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kgd':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Хусаенова Гузель Динаровна\nНомер кабинета: 206'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'ggf':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Гагарина Гульнур Фатрахмановна\nНомер кабинета: 228'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'iau':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Имамеева Алина Юнусовна\nE-mail: AlJSadykova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    # elif call.data == 'mdm':
    #     bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
    #     msg = 'Малмыгина Долорес Махмуриевна\nНомер кабинета: 306\nE-mail: DMMalmygina@kpfu.ru'
    #     bot.send_message(call.message.chat.id, msg)
    elif call.data == 'mfm':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Мухаметшин Фанис Мухаметгалиевич\nНомер кабинета: 308\nE-mail: DMMalmygina@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'tfa':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Тазиева Флюра Ахтамовна\nНомер кабинета: 216'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kgf':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Харисова Гульназ Фаритовна\nНомер кабинета: 318\nE-mail: GFHarisova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'zov':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Залялиева Ольга Владимировна\nНомер кабинета: УНИКС\nE-mail: olgazal65@mail.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kvr':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Кашафутдинов Владислав Ренартович\nНомер кабинета: УНИКС\nE-mail: vkashafutdinov@gmail.com'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'roo':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Романенко Олег Олегович\nЗаместитель директора по воспитательной работе\nНомер кабинета: 135\n' \
              'E-mail: OORomanenko@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'kaa3':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Хавкина Ирина Александровна\nЗаместитель директора по учебной работе\n' \
              'E-mail: IAMalmygina@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'srf':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Самерханова Резида Фаатовна\nЗаместитель директора по административно-хозяйственной работе\n' \
              'Номер кабинета: 1.1\n' \
              'E-mail: RFSamerhanova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'drm':
        bot.send_photo(call.message.chat.id, open(current_directory, 'rb'))
        msg = 'Даминова Раиса Махмуриевна\nЗаместитель директора по учебной работе\n' \
              'Номер кабинета: 110\n' \
              'E-mail: RMDaminova@kpfu.ru'
        bot.send_message(call.message.chat.id, msg)


# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)
