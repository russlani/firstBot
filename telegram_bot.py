import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(
    token=config('TOKEN_BOT')
)


@bot.message_handler(commands=["start", "hi", "Hi"])
def answer_start(message):
    text = f"Добро пожаловат в бота!!! {message.from_user.first_name} " \
           f"{message.from_user.last_name}!!! " \
           f"Выберите тот курс на который хотите пойти"
    keyboard_in = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton(text='python', callback_data='python')
    btn_2 = types.InlineKeyboardButton(text='java', callback_data='java')
    keyboard_in.add(btn_1, btn_2)
    bot.send_message(message.chat.id, text, reply_markup=keyboard_in)


@bot.callback_query_handler(func=lambda call: True)
def send_cource(call):
    if call.data == 'python':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('python morning')
        btn_2 = types.KeyboardButton('python evening')
        btn_3 = types.KeyboardButton('python bootcamp')
        murkup_reply.add(btn_1, btn_2, btn_3)
        text = f'Вы выбрали  {call.data}! Теперь' \
               f' необходимо выбрать группу!!!'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )
    elif call.data == 'java':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_1 = types.KeyboardButton('java')
        btn_2 = types.KeyboardButton('javascript')
        murkup_reply.add(btn_1, btn_2)
        text = f'Вы выбрали  {call.data}! Теперь' \
               f' необходимо выбрать группу!!!'
        bot.send_message(call.message.chat.id, text,
                         reply_markup=murkup_reply
                         )


@bot.message_handler(content_types=['text'])
def send_good_message(message):
    if message.text == 'python morning':
        bot.send_message(
            message.chat.id,
            'вас записали на курс python morning!'
            ' Менеджер с вами свяжится!')
    if message.text == 'python evening':
        bot.send_message(
            message.chat.id,
            'вас записали на курс python evening!'
            ' Менеджер с вами свяжится!')
    if message.text == 'python bootcamp':
        bot.send_message(
            message.chat.id,
            'вас записали на курс python bootcamp!'
            ' Менеджер с вами свяжится!')
    if message.text == 'java':
        bot.send_message(
            message.chat.id,
            'вас записали на курс java!'
            ' Менеджер с вами свяжится!')
    if message.text == 'javascript':
        bot.send_message(
            message.chat.id,
            'вас записали на курс javascript!'
            ' Менеджер с вами свяжится!')

bot.polling()
