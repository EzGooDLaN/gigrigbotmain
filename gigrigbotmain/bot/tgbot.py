import telebot
from telebot import types
import random

bot = telebot.TeleBot("8308147921:AAGDd7d5k6ontWcMQsv8wfYpVXoxe-OXy6o")

answers = ['Я не понял, что ты хочешь сказать.',
           'Извини, я тебя не понимаю.',
           'Я не знаю такой команды.']


@bot.message_handler(commands=['start', 'main', 'hello'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('💶 Варианты заработка')
    button2 = types.KeyboardButton('📄 Отзывы')
    markup.row(button1)
    markup.row(button2)

    if message.text == '/start':
        bot.send_message(message.chat.id, f'Добро пожаловать в GigRig!, {message.from_user.first_name}✨!\n'
                                          f'\n'
                                          f'Наша цель — твой быстрый старт во фрилансе.\n'
                                          f'Мы найдем идеальные заказы,'
                                          f'чтобы ты не тратил время на поиск и шел к финансовым целям максимально эффективно. 📈\n'
                                          f'Начинай с нуля и развивайся вместе с нами. Выбирай комфорт и удаленную работу. Работай головой, а не руками! 💡💻',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!',
                         reply_markup=markup)


@bot.message_handler()
def info(message):
    if message.text == '💶 Варианты заработка':
        catalogChapter(message)
    elif message.text == '📄 Отзывы':
        infoChapter(message)
    elif message.text == '🪙 Оставлять отзывы 🪙':
        reviewsoffer(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '🪙  Оформление карты  🪙':
        applycardoffer(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '🪙  Оформление РКО  🪙':
        RKOoffer(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад'),
        markup.row(button1)
    elif message.text == '🪙 Рассылка сообщений 🪙':
        sendmessoffer(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('↩️ Назад')
        markup.row(button1)
    elif message.text == '↩️ Назад':
        catalogChapter(message)
    elif message.text == '↷ Назад':
        applycardoffer(message)
    elif message.text == '↲ Назад':
        reviewsoffer(message)
    elif message.text == '⤵ Назад':
        sendmessoffer(message)
    elif message.text == '⤵️ Назад':
        RKOoffer(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


def catalogChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🪙 Оставлять отзывы 🪙')
    button2 = types.KeyboardButton('🪙  Оформление карты  🪙')
    button3 = types.KeyboardButton('🪙  Оформление РКО  🪙')
    button4 = types.KeyboardButton('🪙 Рассылка сообщений 🪙')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)
    bot.send_message(message.chat.id, 'Выберите направление заработка:',
                     reply_markup=markup)


def applycardoffer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад')
    markup.row(button1)
    bot.send_photo(message.chat.id, open('images/myphoto.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Заработок на оформлении карт 💸💳\n'
                                      '\n'
                                      'Идеальное направление для людей умеющих предлагать и продавать! '
                                      'Главная цель — найти человека, который сделает карту по твоей ссылке. \n'
                                      'Важно понимать, что с нами вы получите больше, чем от банка!\n'
                                      '\n'
                                      '•  Сложность: Средняя (5/10)\n'
                                      '•  Опыт: Не требуется\n'
                                      '•  Инструменты: Только телефон или ПК\n'
                                      '<a href="https://t.me/managerGigRig">Помощь и ответы на вопросы по работе💻👨‍🔧</a>\n'
                                      'Работаем головой, а не руками! 💡',
                     parse_mode='HTML',
                     reply_markup=markup)


def reviewsoffer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад')
    markup.row(button1)
    bot.send_photo(message.chat.id, open('images/otzivi.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Заработок на отзывах 📑\n'
                                      '\n'
                                      'Идеальное направление для новичков! Здесь не нужны навыки \n'
                                      'Главная цель — найти, людей которые готовы за спасибо написать один отзыв! \n'
                                      'Текст мы выдаем сами, останется просто скопировать и вставить.\n'
                                      '\n'
                                      '•  Сложность: Низкая (0/10)\n'
                                      '•  Опыт: Не требуется\n'
                                      '•  Инструменты: Только телефон или ПК\n'
                                      '<a href="https://t.me/managerGigRig">Помощь и ответы на вопросы по работе💻👨‍🔧</a>\n'
                                      'Работаем головой, а не руками! 💡',
                     parse_mode='HTML',
                     reply_markup=markup)


def sendmessoffer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад')
    markup.row(button1)
    bot.send_photo(message.chat.id, open('images/messa.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Заработок на рассылке сообщений! 📑\n'
                                      '\n'
                                      'Идеальное направление для новичков! Здесь не нужны навыки\n'
                                      'Главная цель — найти, людей которые готовы написать 15 сообщений под разные видео в TikTok!\n'
                                      'Текст мы выдаем сами, останется просто скопировать и вставить.'
                                      '\n'
                                      '•  Сложность: Низкая (0/10)\n'
                                      '•  Опыт: Не требуется\n'
                                      '•  Инструменты: Только телефон или ПК\n'
                                      '\n'
                                      '<a href="https://t.me/managerGigRig">Помощь и ответы на вопросы по работе💻👨‍🔧</a>\n'
                                      'Работаем головой, а не руками! 💡',
                     parse_mode='HTML',
                     reply_markup=markup)


def RKOoffer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('↩️ Назад')
    markup.row(button1)
    bot.send_photo(message.chat.id, open('images/rko.jpg', 'rb'))
    bot.send_message(
        message.chat.id,
        'Заработок на оформлении РКО💸\n'
        '\n'
        'Идеальное направление для людей желающих быстро заработать не вкладываясь!\n'
        'Главная задача — оформить РКО в банке.\n'
        'Это не самое легкое задание, но очень хорошо оплачиваемое\n'
        '\n'
        '•  Сложность: Хард (9/10)\n'
        '•  Опыт: Не требуется\n'
        '•  Инструменты: Только телефон или ПК\n'
        '❗ Важно чтобы вы были старше 18 лет❗\n'
        '\n'
        '<a href="https://t.me/managerGigRig">Помощь и ответы на вопросы по работе💻👨‍🔧</a>\n'
        'Работаем головой, а не руками! 💡',
        parse_mode='HTML',
        reply_markup=markup)


def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, 'Раздел с отзывами от реальных пользователей!\n'
                                      't.me/otzivgigrig', reply_markup=markup)


bot.polling(none_stop=True)
