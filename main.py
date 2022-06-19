from bs4 import BeautifulSoup
import telebot
import requests


response = requests.get("https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=996&brands[0][generation]=1996&body_type[0]=2&engine_type[0]=1&engine_type[1]=2&engine_type[2]=3&engine_type[3]=4")
soup = BeautifulSoup(response.content, "html.parser")
a_title = soup.find_all(class_="listing-item__link")

bot = telebot.TeleBot('5519264442:AAGpijRs82bJa5fwiSDRyc9bi_tpQw8L3x8')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я Твой помощник. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'help':
        bot.send_message(message.from_user.id, "Это Bot для парсинга")
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, "Привет")
    if message.text.lower() == 'как дела?':
        bot.send_message(message.from_user.id, 'Спасибо всё хорошо!')
    if message.text.lower() == 'av':
        for item in a_title:

            item_href = "https://cars.av.by" + item.get("href")
            bot.send_message(message.from_user.id, item_href)

bot.polling(none_stop=True)