import telebot
import mytoken
from mytoken import keys, TOKEN
from extensions import Converter, APIException

bot = telebot.TeleBot(mytoken.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в формате : \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \nУвидить список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text += '.\n-' + key
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    bot.reply_to(message, f"Мне в падлу смотреть")
    pass

@bot.message_handler(content_types=['voice'])
def repeat_voice(message: telebot.types.Message):
    bot.reply_to(message, "Лучше не говори, ПРОТИВНО!")

@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Что за собака Сутулая')

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    if message.text == "/start":
        return
    if message.text == "/help":
        return
    if message.text == "/values":
        return

    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Недостаточно параметров для конвертации.')

        quote, base, amount = values
        total_base = Converter.get_price(quote, base, amount)
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')

bot.polling(none_stop=True)

