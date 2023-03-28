import telebot, time
from telebot import types

bot = telebot.TeleBot("5970407370:AAHWHdPZm5fGoDYrp4KFA9SmREn4N3MtVaw")
product = {}
channels = []


@bot.message_handler(commands=["start"])
def start(message):
  blacklist = open("blacklist.txt", "r")
  file_contents = blacklist.read()
  if message.chat.type == "private" and not (
    (str(message.from_user.username)) in file_contents):
    if message.chat.id == 5875900979:
      markup = types.InlineKeyboardMarkup()
      btn1 = types.InlineKeyboardButton("Создать пост",
                                        callback_data="create_post")
      btn2 = types.InlineKeyboardButton("Добавить группу",
                                        callback_data="add_channel")
      btn3 = types.InlineKeyboardButton("Удалить группу",
                                        callback_data="delete_channel")
      btn4 = types.InlineKeyboardButton("Черный список",
                                        callback_data="blacklist")
      markup.row_width = 1
      markup.add(btn1, btn2, btn3, btn4)
      bot.send_message(message.chat.id,
                       text=f"Приветствую, {message.chat.first_name}!"
                       "\nВот список того что я умею",
                       reply_markup=markup)
    elif not (bot.get_chat_member(chat_id=-1001501318566,
                                  user_id=message.chat.id)).status == "left":
      markup = types.InlineKeyboardMarkup()
      btn1 = types.InlineKeyboardButton("🆘Помощь", callback_data="help")
      btn2 = types.InlineKeyboardButton("🛟Проблема с заказом",
                                        callback_data="Problem")
      markup.row_width = 1
      markup.add(btn1, btn2)
      bot.send_message(message.chat.id,
                       text="ПРИВЕТ, " + message.chat.first_name + " \!"
                       "\n\nЯ, бот\-поддержки магазина СНЕГОПАД ❄"
                       "\nЕсть вопрос по заказу или предложение о "
                       "сотрудничестве? "
                       "\nВоспользуйся кнопками ниже, и мы ответим "
                       "Вам в ближайшее время\. "
                       "\n\n\n\nУ тебя спам и не можешь написать "
                       "НАМ? 👉[ЖМИ](http://t.me/AntiSPAMsnow_bot)👈 "
                       "\n\n❗НАБОР В КОМАНДУ СНЕГОПАД❗"
                       "\nВакансии:"
                       "\n–ОПЕРАТОР"
                       "\n–КЛАДМЕН"
                       "\nОставляй заявку с отметкой «РАБОТА» "
                       "первым словом\.",
                       parse_mode="MarkdownV2",
                       reply_markup=markup)
    else:
      markup = types.InlineKeyboardMarkup()
      btn1 = types.InlineKeyboardButton("↗️Перейти и подписаться",
                                        url="https://t.me/+9dZaK6TiamM3MDJi")
      btn2 = types.InlineKeyboardButton("Проверить", callback_data="proverka")
      markup.add(btn1)
      markup.add(btn2)
      bot.send_message(message.chat.id,
                       "📰Обязательным условием данного бота является подписка "
                       "на [нас](https://t.me/+9dZaK6TiamM3MDJi)\.",
                       parse_mode="MarkdownV2",
                       reply_markup=markup)
  else:
    bot.send_message(message.chat.id, "Вы добавлены в черный список")


def menu(message):
  if message.chat.id == 5875900979:
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Создать пост",
                                      callback_data="create_post")
    btn2 = types.InlineKeyboardButton("Добавить группу",
                                      callback_data="add_channel")
    btn3 = types.InlineKeyboardButton("Удалить группу",
                                      callback_data="delete_channel")
    btn4 = types.InlineKeyboardButton("Черный список",
                                      callback_data="blacklist")
    markup.row_width = 1
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     text="Вот список того что я умею",
                     reply_markup=markup)

  else:
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🆘Помощь", callback_data="help")
    btn2 = types.InlineKeyboardButton("🛟Проблема с заказом",
                                      callback_data="Problem")
    markup.row_width = 1
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Вот список того что я умею",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "help")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("Вернуться назад", callback_data="1_back")
  btn2 = types.InlineKeyboardButton("Да", callback_data="tp")
  markup.add(btn1, btn2)
  bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text="Пожалуйста, обратите внимание, на график работы \n"
    "ОПЕРАТОРА. Мы стараемся ответить вам, как можно быстрее, но ожидание может занять "
    "ВРЕМЯ. "
    "\nНе создавайте повторный запрос на эту заявку - ваша заявка автоматически уйдёт вниз "
    "и вам придётся ждать дольше."
    "\n\nГрафик работы оператора: 13:00-03:00 НСК. 7,14,21,28 - выходной.",
    reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "tp")
def callback_inline(call):
  bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text="Скажите что мне нужно передать")
  bot.register_next_step_handler(call.message, tp)


def tp(message):
  bot.send_message(
    5875900979, text=f"Сообщение от @{message.chat.username}\n{message.text}")
  bot.send_message(
    message.chat.id,
    "Уже передал вашу проблему! Ожидайте в ближайшее время сообщение от оператора😉"
  )
  menu(message)


@bot.callback_query_handler(func=lambda call: call.data == "1_back")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("🆘Помощь", callback_data="help")
  btn2 = types.InlineKeyboardButton("🛟Проблема с заказом",
                                    callback_data="Problem")
  markup.row_width = 1
  markup.add(btn1, btn2)
  bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text="ПРИВЕТ, " + call.message.chat.first_name + " \!"
                        "\n\nЯ, бот\-поддержки магазина СНЕГОПАД ❄"
                        "\nЕсть вопрос по заказу или предложение о "
                        "сотрудничестве? "
                        "\nВоспользуйся кнопками ниже, и мы "
                        "ответим Вам в ближайшее время\. "
                        "\n\n\n\nУ тебя спам и не можешь написать "
                        "НАМ? 👉[ЖМИ]("
                        "http://t.me/AntiSPAMsnow_bot)👈 "
                        "\n\n❗НАБОР В КОМАНДУ СНЕГОПАД❗"
                        "\nВакансии:"
                        "\n–ОПЕРАТОР"
                        "\n–КЛАДМЕН"
                        "\nОставляй заявку с отметкой «РАБОТА» "
                        "первым словом\.",
                        parse_mode="MarkdownV2",
                        reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "Problem")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("💎Senior Crystal💎",
                                    callback_data="Product1")
  btn2 = types.InlineKeyboardButton("🍫Ice-o-lator DCI🍫",
                                    callback_data="Product2")
  btn3 = types.InlineKeyboardButton("🥦BOSHKI GIRLSCOUT cookies🥦",
                                    callback_data="Product3")
  btn4 = types.InlineKeyboardButton("❄️☆МЕФ☆ [МУКА]❄️",
                                    callback_data="Product4")
  btn5 = types.InlineKeyboardButton("💣ГАШ Ice-o-lator BabyGIRL💣",
                                    callback_data="Product5")
  markup.row_width = 1
  markup.add(btn1, btn2, btn3, btn4, btn5)
  bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text=
    "Если у тебя произошли какие либо ПРОБЛЕМЫ с заказом, прочитай *ВНИМАТЕЛЬНО*\!👇"
    "\n\nПРОБЛЕМЫ С ОПЛАТОЙ? ПИСАТЬ В TELEGRAM : \n@babushkahelpbot"
    "\n\nПри ненаходе, не забудь сделать фото места, фото поисков, не забудь указать все "
    "важные детали\."
    "\n\nПокупателем с 1 покупкой в перезакладе будет отказано\!"
    "\n\nЕсли покупатель будет слишком агрессивный \(оскорбляет магазин или его "
    "работников\), "
    "в перезакладе будет отказано\."
    "\n\n[Не знание правил магазина \- не освобождает от наказания\.]("
    "https://telegra.ph/%E3%85%A4%E3%85%A4%E3%85%A4-11-19-4) "
    "\n\n*ЧТОБЫ ОТКРЫТЬ ДИСПУТ:*"
    "\n\nДЛЯ начала выберите свою позицию ниже, *КАК В БОТЕ* \-",
    reply_markup=markup,
    disable_web_page_preview=True,
    parse_mode="MarkdownV2")


@bot.callback_query_handler(func=lambda call: call.data == "Product1")
def callback_inline(call):
  product[str(call.message.chat.id)] = []
  product[str(call.message.chat.id)].append(str("Товар: Senior Crystal"))
  bot.send_message(
    call.message.chat.id,
    "*❗️\!\!\! ВНИМАНИЕ \!\!\!❗️\nВведите номер вашей заявки \(id\) "
    "который вам выдал бот продаж с реквизитами на оплату — он "
    "состоит из 8 цифр и начинается с цифры 1\.*",
    parse_mode="MarkdownV2")
  bot.register_next_step_handler(call.message, application)


@bot.callback_query_handler(func=lambda call: call.data == "Product2")
def callback_inline(call):
  product[str(call.message.chat.id)] = []
  product[str(call.message.chat.id)].append(str("Товар: Ice-o-lator DCI"))
  bot.send_message(
    call.message.chat.id,
    "*❗️\!\!\! ВНИМАНИЕ \!\!\!❗️\nВведите номер вашей заявки \(id\) "
    "который вам выдал бот продаж с реквизитами на оплату — "
    "он состоит из 8 цифр и начинается с цифры 1\.*",
    parse_mode="MarkdownV2")
  bot.register_next_step_handler(call.message, application)


@bot.callback_query_handler(func=lambda call: call.data == "Product3")
def callback_inline(call):
  product[str(call.message.chat.id)] = []
  product[str(call.message.chat.id)].append(
    str("Товар: BOSHKI GIRLSCOUT cookies"))
  bot.send_message(
    call.message.chat.id,
    "*❗️\!\!\! ВНИМАНИЕ \!\!\!❗️\nВведите номер вашей заявки \(id\) "
    "который вам выдал бот продаж с реквизитами на оплату — "
    "он состоит из 8 цифр и начинается с цифры 1\.*",
    parse_mode="MarkdownV2")
  bot.register_next_step_handler(call.message, application)


@bot.callback_query_handler(func=lambda call: call.data == "Product4")
def callback_inline(call):
  product[str(call.message.chat.id)] = []
  product[str(call.message.chat.id)].append(str("Товар: МЕФ [МУКА]"))
  bot.send_message(
    call.message.chat.id,
    "*❗️\!\!\! ВНИМАНИЕ \!\!\!❗️\nВведите номер вашей заявки \(id\) "
    "который вам выдал бот продаж с реквизитами на оплату — "
    "он состоит из 8 цифр и начинается с цифры 1\.*",
    parse_mode="MarkdownV2")
  bot.register_next_step_handler(call.message, application)


@bot.callback_query_handler(func=lambda call: call.data == "Product5")
def callback_inline(call):
  product[str(call.message.chat.id)] = []
  product[str(call.message.chat.id)].append(
    str("Товар: ГАШ Ice-o-lator BabyGIRL"))
  bot.send_message(
    call.message.chat.id,
    "*❗️\!\!\! ВНИМАНИЕ \!\!\!❗️\nВведите номер вашей заявки \(id\) "
    "который вам выдал бот продаж с реквизитами на оплату — "
    "он состоит из 8 цифр и начинается с цифры 1\.*",
    parse_mode="MarkdownV2")
  bot.register_next_step_handler(call.message, application)


def application(message):
  product[str(message.chat.id)].append(
    str(f"Номер заявки на оплату: {message.text}"))
  bot.send_message(message.chat.id,
                   "Опишите подробно вашу проблему и я ее передам")
  bot.register_next_step_handler(message, application1)


def application1(message):
  product[str(message.chat.id)].append(str(message.text))
  case = ""
  for i in product.get(str(message.chat.id)):
    case += i + "\n"
  bot.send_message(
    5875900979, text=f"☑Новое обращение от @{message.chat.username}\n\n{case}")
  bot.send_message(
    message.chat.id,
    "Ваше обращение отправлено! Мы вам напишем в ближайшее время")
  del product[str(message.chat.id)]
  menu(message)


@bot.callback_query_handler(func=lambda call: call.data == "create_post")
def callback_inline(call):
  if not len(channels) == 0:
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
    markup.add(btn1)
    case = ""
    for i in channels:
      case += i.title + "\n"
    bot.edit_message_text(
      chat_id=call.message.chat.id,
      message_id=call.message.message_id,
      text=
      f"Перешлите мне нужный пост. Его я разошлю по следующим группам: \n{case}",
      reply_markup=markup)
    bot.register_next_step_handler(call.message, mailing)

  else:
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Добавить группу",
                                      callback_data="add_channel")
    btn2 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
    markup.row_width = 1
    markup.add(btn1, btn2)
    bot.edit_message_text(
      chat_id=call.message.chat.id,
      message_id=call.message.message_id,
      text=
      "Здесь пока нет каналов. Вы можете их добавить в соответствующем меню:",
      reply_markup=markup)


def mailing(message):
  for e in channels:
    bot.forward_message(e.id, message.chat.id, message.message_id)
  bot.send_message(message.chat.id, "Рассылка по группам прошла успешно✅")
  menu(message)


@bot.callback_query_handler(func=lambda call: call.data == "2_back")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("Создать пост",
                                    callback_data="create_post")
  btn2 = types.InlineKeyboardButton("Добавить группу",
                                    callback_data="add_channel")
  btn3 = types.InlineKeyboardButton("Удалить группу",
                                    callback_data="delete_channel")
  btn4 = types.InlineKeyboardButton("Черный список", callback_data="blacklist")
  markup.row_width = 1
  markup.add(btn1, btn2, btn3, btn4)
  bot.edit_message_text(chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=f"Приветствую, {call.message.chat.first_name}! "
                        "\nВот список того что я умею",
                        reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == "add_channel")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
  markup.add(btn1)
  bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text=
    "Перешлите сюда сообщение из группы, которую вы хотите добавить\.\n\n*Важно:* бот "
    "должен быть администратором в группе из которого вы пересылаете сообщение, а так же "
    "сообщение должно быть отправлено от имени группы\(анонимно\)\.",
    parse_mode="MarkdownV2",
    reply_markup=markup)
  bot.register_next_step_handler(call.message, add_channel)


def add_channel(message):
  if message.forward_from_chat is None:
    bot.send_message(message.chat.id, "Это не похоже на форвард.")
    menu(message)
  elif message.forward_from_chat in channels:
    bot.send_message(message.chat.id, "Эта группа уже есть в списке")
    menu(message)
  else:
    bot.send_message(
      message.chat.id,
      f"Канал {message.forward_from_chat.title} успешно добавлен 🎉")
    channels.append(message.forward_from_chat)
    menu(message)


@bot.callback_query_handler(func=lambda call: call.data == "delete_channel")
def callback_inline(call):
  if not channels == ():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
    markup.add(btn1)
    case = ""
    for i in channels:
      case += i.title + "\n"
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text=f"Выберите канал для удаления:\n{case}",
                          reply_markup=markup)
    bot.register_next_step_handler(call.message, delete)
  else:
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Добавить группу",
                                      callback_data="add_channel")
    btn2 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
    markup.row_width = 1
    markup.add(btn1, btn2)
    bot.edit_message_text(
      chat_id=call.message.chat.id,
      message_id=call.message.message_id,
      text=
      "Здесь пока нет каналов. Вы можете их добавить в соответствующем меню:",
      reply_markup=markup)


def delete(message):
  for i in channels:
    if i.title == message.text:
      channels.pop(channels.index(i))
      bot.send_message(message.chat.id, "Канал удален☑")
  menu(message)


@bot.callback_query_handler(func=lambda call: call.data == "blacklist")
def callback_inline(call):
  markup = types.InlineKeyboardMarkup()
  btn1 = types.InlineKeyboardButton("🔙Вернуться", callback_data="2_back")
  markup.add(btn1)
  bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text=
    "Напишите никнейм пользователя без @, которого нужно добавить в черный список бота.",
    reply_markup=markup)
  bot.register_next_step_handler(call.message, add_blacklist)


def add_blacklist(message):
  blacklistFile = open("blacklist.txt", "w")
  blacklistFile.write(str(message.text))
  bot.send_message(message.chat.id, "Пользователь добавлен в черный список")


@bot.callback_query_handler(func=lambda call: call.data == "proverka")
def callback_inline(call):
  if not (bot.get_chat_member(chat_id=-1001501318566,
                              user_id=call.message.chat.id)).status == "left":
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🆘Помощь", callback_data="help")
    btn2 = types.InlineKeyboardButton("🛟Проблема с заказом",
                                      callback_data="Problem")
    markup.row_width = 1
    markup.add(btn1, btn2)
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="ПРИВЕТ, " + call.message.chat.first_name +
                          " \!"
                          "\n\nЯ, бот\-поддержки магазина "
                          "СНЕГОПАД ❄ "
                          "\nЕсть вопрос по заказу или "
                          "предложение о сотрудничестве? "
                          "\nВоспользуйся кнопками ниже, и мы "
                          "ответим Вам в ближайшее время\. "
                          "\n\n\n\nУ тебя спам и не можешь "
                          "написать НАМ? 👉[ЖМИ]("
                          "http://t.me/AntiSPAMsnow_bot)👈 "
                          "\n\n❗НАБОР В КОМАНДУ СНЕГОПАД❗"
                          "\nВакансии:"
                          "\n–ОПЕРАТОР"
                          "\n–КЛАДМЕН"
                          "\nОставляй заявку с отметкой «РАБОТА» "
                          "первым словом\.",
                          parse_mode="MarkdownV2",
                          reply_markup=markup)


if __name__ == "__main__":
  while True:
    try:
      bot.polling(none_stop=True)
    except Exception as e:
      time.sleep(3)
      print(e)
