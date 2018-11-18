import telebot
from telebot import types

TOKEN = '552113433:AAGFhzXdX8ZTK91cOo00cm5t4uAXbB1N1v8'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Русский", callback_data="rus")
    but_2 = types.InlineKeyboardButton(text="O'zbekcha", callback_data="uz")
    keyboard.add(but_1, but_2)
    bot.send_message(message.chat.id, "*Выберите язык*👇\nTilni"
                                      " tanlang👇", reply_markup=keyboard, parse_mode='markdown')


@bot.callback_query_handler(func=lambda m: True)
def reply(c):
    if c.data == "uz":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Haydovchi bo'lish 🚕", callback_data="1")
        but_2 = types.InlineKeyboardButton(text="☎️ Tex.aloqa ☎️", callback_data="2")
        but_3 = types.InlineKeyboardButton(text="Yordamℹ️", callback_data="3")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Haydovchilarni Yandex.Taxi ga ulash uchun Toshkentdagi ofisial botga hush "
                                   "kelibsiz!🚕\n "
                                   "\n"
                                   "Botimizdan qanday foydalanishni bilib olish uchun *Yordam*ℹ️ tugmasini bosing.",
                              reply_markup=keyboard, parse_mode='markdown')
    if c.data == "1":
        first = bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="O'zingizning telefon raqamingizni +998 9X XXX XX XX formatida bizga jo'nating. Bu raqamingiz "
                 "Taksometr programmangizga ulaniladi...\n\n"
                 "Raqamingizni bizga jo'natib bo'lganingizdan so'ng ""*Keyingisi* ➡️"" "
                 "tugmasini bosing ", parse_mode='markdown')
        bot.register_next_step_handler(first, msg)
    if c.data == "2":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Bosh menyu", callback_data="Bosh")
        keyboard.add(but_1)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text='🚕🚕🚕🚕🚕🚕🚕🚕\n\nAgar botimiz ishlashida hatoliklar '
                                   'bo''lsa, yoki bo''timiz qanday ishlashini tushunmayotgan bo''lsangiz '
                                   'bizning Tex.aloqamizga qo''ng''iroq qiling☎️:\n\n+998977450440\n\n+'
                                   '998974619797\n\nTelegramimiz: @SMARTWAYTRANS\n\n🚕🚕🚕🚕🚕🚕🚕🚕',
                              reply_markup=keyboard)
    if c.data == "3":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Bosh menyu", callback_data="Bosh")
        keyboard.add(but_1)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Нажмите на кнопку ""*🚕 Haydovchi bo'lish 🚕*"" tugmasini bosing va u yerda yozgan "
                                   "ko'rsatmalarimizga amal qiling.\n\n"
                                   "Hozir esa ""*Bosh menyu*"" tugmasini bosing va bosh menyuga qayting."
                                   "\n\n"
                                   "\n"
                                   "Agar tushunmayotgan bo'lsangiz "
                                   "bizga yozing → @SMARTWAYTRANS\n\n"
                                   "Powered by Smart Taxi🚖",
                              reply_markup=keyboard, parse_mode='markdown')
    if c.data == "Bekor":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Haydovchi bo'lish 🚕", callback_data="1")
        but_2 = types.InlineKeyboardButton(text="☎️ Tex.aloqa ☎️", callback_data="2")
        but_3 = types.InlineKeyboardButton(text="Yordamℹ️", callback_data="3")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Va yana bir bora haydovchilarni Yandex.Taxi ga ulash uchun Toshkentdagi ofisial "
                                   "botga hush kelibsiz!🚕\n"
                                   "\n"
                                   "Botimizdan qanday foydalanishni bilib olish uchun *Yordam*ℹ️ tugmasini bosing.",
                              reply_markup=keyboard, parse_mode='markdown')
    if c.data == "Keyingisi":
        second = bot.edit_message_text(chat_id=c.message.chat.id,
                                       message_id=c.message.message_id,
                                       text="Endi esa, haydovchilik guvohnomangizni old tomonini rasimga olib botga "
                                            "yuboring.\n\nBotga rasmni yuborib bo'lganingizdan "
                                            "so'ng ""*Keyingisi*"" tugmasini "
                                            "bosing...", parse_mode='markdown')
        bot.register_next_step_handler(second, finish)
    if c.data == "1Keyingisi":
        seventh = bot.edit_message_text(chat_id=c.message.chat.id,
                                        message_id=c.message.message_id,
                                        text="Endi esa, tex.pasportingizni old tomonini rasimga olib botga "
                                             "yuboring.\n\nBotga rasmni yuborib bo'lganingizdan "
                                             "so'ng ""*Keyingisi*"" tugmasini "
                                             "bosing...", parse_mode='markdown')
        bot.register_next_step_handler(seventh, finish0)
    if c.data == "2Keyingisi":
        eighth = bot.edit_message_text(chat_id=c.message.chat.id,
                                       message_id=c.message.message_id,
                                       text="Endi esa, tex.pasportingizni orqa tomonini rasimga olib botga "
                                            "yuboring.\n\nBotga rasmni yuborib bo'lganingizdan "
                                            "so'ng ""*Tayyor*"" tugmasini "
                                            "bosing...", parse_mode='markdown')
        bot.register_next_step_handler(eighth, finish01)
    if c.data == "Tayyor":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Bosh menyu", callback_data="Bosh")
        but_sw = types.InlineKeyboardButton(text='Ulashish', switch_inline_query="👈 Haydovchilarni Yandex Taksiga 1 "
                                                                                 "daqiqada ulab beradigan "
                                                                                 "telegram bot!")
        key.add(but_1)
        key.add(but_sw)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Yashasin!!!\nTabriklaymiz qadrli haydovchi, sizning ma'lumotlaringizni ko'rib "
                                   "chiqmoqdamiz! "
                                   "Yaqin daqiqalarda siz bilan aloqaga chiqamiz.\n\n"
                                   "Agag sizga botimiz yoqgan bo'lsa *Ulashish* tugmasini bosing va do'stlaringizga "
                                   "ulashing👇", reply_markup=key, parse_mode='markdown')
    if c.data == "Bosh":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Haydovchi bo'lish 🚕", callback_data="1")
        but_2 = types.InlineKeyboardButton(text="☎️ Tex.aloqa ☎️", callback_data="2")
        but_3 = types.InlineKeyboardButton(text="Yordamℹ️", callback_data="3")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.send_message(c.message.chat.id,
                         " Va yana bir bora haydovchilarni Yandex.Taxi ga ulash uchun Toshkentdagi ofisial "
                         "botga hush kelibsiz!🚕\n"
                         "\n"
                         "Botimizdan qanday foydalanishni bilib olish uchun *Yordam*ℹ️ tugmasini bosing.",
                         reply_markup=keyboard, parse_mode='markdown')
    if c.data == "rus":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Стать водителем 🚕", callback_data="🚕 Стать водителем 🚕")
        but_2 = types.InlineKeyboardButton(text="☎️ Тех.поддержка ☎️", callback_data="☎️ Тех.поддержка ☎️")
        but_3 = types.InlineKeyboardButton(text="Помощьℹ️", callback_data="Помощьℹ️")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Добро пожаловать в официальный бот для подключения водителей к Яндекс.Такси в Ташкенте!🚕\n"
                 "\n"
                 "Нажмите на кнопку ""*Помощь*ℹ️"", чтобы узнать как пользоваться ботом.",
            reply_markup=keyboard, parse_mode='markdown')
    if c.data == "🚕 Стать водителем 🚕":
        third = bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text="Напишите нам свой номер телефона в формате +998 9X XXX "
                 "XX XX "
                 ", чтобы привязать его к "
                 "программе Таксометр...\n\n"
                 "После того как вы отправили свой номер, "
                 "нажмите на кнопку ""*Далее* ➡️""", parse_mode='markdown')
        bot.register_next_step_handler(third, msg1)
    if c.data == "Отмена⬅️":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Стать водителем 🚕", callback_data="🚕 Стать водителем 🚕")
        but_2 = types.InlineKeyboardButton(text="☎️ Тех.поддержка ☎️", callback_data="☎️ Тех.поддержка ☎️")
        but_3 = types.InlineKeyboardButton(text="Помощьℹ️", callback_data="Помощьℹ️")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Снова Рады вас видеть в официальном боте для подключения водителей к "
                                   "Яндекс.Такси!🚕!\n "
                                   "\n"
                                   "Нажмите на кнопку ""*Помощь*ℹ️"", чтобы узнать как пользоваться ботом.",
                              reply_markup=keyboard, parse_mode='markdown')
    if c.data == "Помощьℹ️":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Главное меню", callback_data="Главное меню")
        keyboard.add(but_1)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Нажмите на кнопку ""*🚕 Стать водителем 🚕*"", и следуйте подсказкам\n\n"
                                   "Сейчас нажмите на кнопку *Главное меню*, чтобы "
                                   "вернуться в главное меню нашего бота."
                                   "\n\n"
                                   "\n"
                                   "Если вы не поняли как пользоваться ботом, "
                                   "напишите нам → @SMARTWAYTRANS\n\n"
                                   "Powered by Smart Taxi🚖",
                              reply_markup=keyboard, parse_mode='markdown')
    if c.data == "Далее ➡️":
        fourth = bot.edit_message_text(chat_id=c.message.chat.id,
                                       message_id=c.message.message_id,
                                       text="Теперь сфотографируйтете переднюю сторону своего водительского "
                                            "удостоверения,"
                                            " "
                                            "затем отправьте этому боту.\n\nПосле того как вы отправили их,"
                                            " нажмите на кнопку ""*Далее*""", parse_mode='markdown')
        bot.register_next_step_handler(fourth, finish1)
    if c.data == "1Далее ➡️":
        fifth = bot.edit_message_text(chat_id=c.message.chat.id,
                                      message_id=c.message.message_id,
                                      text="Теперь сфотографируйтете переднюю сторону своего тех.паспорта, затем "
                                           "отправьте этому боту.\n\nПосле того как вы отправили их,"
                                           " нажмите на кнопку ""*Далее*""", parse_mode='markdown')
        bot.register_next_step_handler(fifth, finish1_2)
    if c.data == '2Далее ➡️':
        sixth = bot.edit_message_text(chat_id=c.message.chat.id,
                                      message_id=c.message.message_id,
                                      text="Теперь сфотографируйтете заднюю сторону своего тех.паспорта, затем "
                                           "отправьте этому боту.\n\nПосле того как вы отправили их,"
                                           " нажмите на кнопку ""*Далее*""", parse_mode='markdown')
        bot.register_next_step_handler(sixth, finish1_2_3)
    if c.data == "Готово":
        key = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Главное меню", callback_data="Главное меню")
        but_sw = types.InlineKeyboardButton(text='Поделиться', switch_inline_query="👈 Телеграм бот для регистрации"
                                                                                   " водитиделей к "
                                                                                   "Яндекс Такси за 1 минуту!")
        key.add(but_1)
        key.add(but_sw)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text="Ура!!!\nПоздравляем дорогой водитель, ваши данные в рассмотрении! "
                                   "В ближайшее время мы сами "
                                   "свяжемся с вами\n\nЕсли вам понравился наш бот, вы можете рекомендовать его своим "
                                   "знакомым и друзьям с помощью кнопки "
                                   """*Поделиться*👇""", reply_markup=key, parse_mode='markdown')
    if c.data == "Главное меню":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="🚕 Стать водителем 🚕", callback_data="🚕 Стать водителем 🚕")
        but_2 = types.InlineKeyboardButton(text="☎️ Тех.поддержка ☎️", callback_data="☎️ Тех.поддержка ☎️")
        but_3 = types.InlineKeyboardButton(text="Помощьℹ️", callback_data="Помощьℹ️")
        keyboard.add(but_1)
        keyboard.add(but_2)
        keyboard.add(but_3)
        bot.send_message(chat_id=c.message.chat.id,
                         text="Снова Рады вас видеть в официальном боте для подключения водителей к "
                              "Яндекс.Такси в Ташкенте!🚕!\n "
                              "\n"
                              "Нажмите на кнопку *Помощь*ℹ️, чтобы узнать как пользоваться ботом.",
                         reply_markup=keyboard, parse_mode='markdown')
    if c.data == "☎️ Тех.поддержка ☎️":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        but_1 = types.InlineKeyboardButton(text="Главное меню", callback_data="Главное меню")
        keyboard.add(but_1)
        bot.edit_message_text(chat_id=c.message.chat.id,
                              message_id=c.message.message_id,
                              text='🚕🚕🚕🚕🚕🚕🚕🚕\n\nЕсли вы нашли ошибку, или у вас есть '
                                   'вопросы по поводу '
                                   'работы бота, '
                                   'то позвоните в нашу Тех.поддержку☎️:\n\n+998977450440\n\n+'
                                   '998974619797\n\nНаш телеграм: @SMARTWAYTRANS\n\n🚕🚕🚕🚕🚕🚕🚕🚕',
                              reply_markup=keyboard)


def msg(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Keyingisi ➡️", callback_data="Keyingisi")
    but_2 = types.InlineKeyboardButton(text="Bekor qilish⬅️", callback_data="Bekor")
    key.add(but_1)
    key.add(but_2)
    bot.send_message(message.chat.id, text='Endi esa `Keyingisi` tugmasini bosing👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Keyingisi ➡️", callback_data="1Keyingisi")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Endi esa `Keyingisi ➡️` tugmasini bosing👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish0(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Keyingisi ➡️", callback_data="2Keyingisi")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Endi esa `Keyingisi ➡️` tugmasini bosing👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish01(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Tayyor", callback_data="Tayyor")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Endi esa `Tayyor` tugmasini bosing👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def msg1(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Далее ➡️", callback_data="Далее ➡️")
    but_2 = types.InlineKeyboardButton(text="Отмена⬅️", callback_data="Отмена⬅️")
    key.add(but_1)
    key.add(but_2)
    bot.send_message(message.chat.id, text='Теперь нажмите на кнопку `Далее`👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish1(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Далее ➡️", callback_data="1Далее ➡️")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Теперь нажмите на кнопку `Далее ➡️`👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish1_2(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Далее ➡️", callback_data="2Далее ➡️")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Теперь нажмите на кнопку `Далее ➡️`👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


def finish1_2_3(message):
    key = types.InlineKeyboardMarkup(row_width=1)
    but_1 = types.InlineKeyboardButton(text="Готово", callback_data="Готово")
    key.add(but_1)
    bot.send_message(message.chat.id, text='Теперь нажмите на кнопку `Готово`👇',
                     reply_markup=key, parse_mode='markdown')
    bot.forward_message('-1001362610462', message.chat.id, message.message_id)


@bot.edited_message_handler(content_types=['text'])
def echo_digits(message):
    bot.send_message(message.chat.id, text='Если вы изменили свой номер телефона, '
                                           'то пожалуйста нажмите на кнопку `Отмена` и отправьте его заново с '
                                           'комментарием.\n\nAgar siz telefon '
                                           ' raqamingizni o''zgartirgan bo''lsangiz, iltimos `Bekor qilish` tugmasini '
                                           'bosing va bizga uni '
                                           'chuntirish bilan qayta yuboring.', parse_mode='markdown')


if __name__ == "__main__":
    bot.polling(none_stop=True)

"""""
def read_contact_data(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона☎️", request_contact=True)
    # button_geo = types.KeyboardButton(text="Отправить местоположение🗺️", request_location=True)
    keyboard.add(button_phone)
    msg = bot.send_message(message.chat.id,
                           "Отправьте боту свой номер телефона для входа в систему! Для этого нажмите на кнопку↓",
                           reply_markup=keyboard)
    bot.register_next_step_handler(msg, process_step)
"""""
