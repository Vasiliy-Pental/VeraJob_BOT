from bs4 import BeautifulSoup
import telebot
import requests
import time


#block av
response = requests.get("https://cars.av.by/filter?brands[0][brand]=989&brands[0][model]=996&brands[0][generation]=1996&body_type[0]=2&engine_type[0]=1&engine_type[1]=2&engine_type[2]=3&engine_type[3]=4")
soup = BeautifulSoup(response.content, "html.parser")
a_title = soup.find_all(class_="listing-item__link")
#token bot
bot = telebot.TeleBot('5519264442:AAGpijRs82bJa5fwiSDRyc9bi_tpQw8L3x8')

#block Vera_bot
url="https://ingamejob.com/en/jobs?cities%5B0%5D=0&profession%5B0%5D=33&q=&page=1"
req = requests.get(url)

with open("vera.html", "w",encoding="utf-8") as file:
    file.write(req.text)
with open("vera.html",encoding="utf-8") as file:
    srce = file.read()

soup = BeautifulSoup(srce,'lxml')
articles = soup.find_all("div",class_="col-12 p-0")


#block hh
url ="https://spb.hh.ru/search/vacancy?clusters=true&employment=full&enable_snippets=true&ored_clusters=true&schedule=fullDay&search_period=7&text=Artist+2d+%D1%85%D1%83%D0%B4%D0%BE%D0%B6%D0%BD%D0%B8%D0%BA&order_by=publication_time&hhtmFrom=vacancy_search_list"
headers = {

        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.366"
    }

reqr = requests.get(url,headers=headers)
#print(reqr.text)
print(reqr.status_code)

with open("projects.html", "w",encoding="utf-8") as file:
    file.write(reqr.text)
with open("projects.html",encoding="utf-8") as file:
    srcc = file.read()

soup = BeautifulSoup(srcc,'lxml')
articles_all = soup.find_all("span",class_=("g-user-content"))
#print(articles)



#for article_sort in articles_all:

    #article_sort_url = article_sort.find("a", class_="bloko-link").get("href")

    #print(article_sort_url)








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


            bot.send_message(message.from_user.id, item_href)
    if message.text.lower() == 'ingame':
        time.sleep(2)
        for article in articles:
            vera_url = article.find("h5",class_="").find("a").get("href")
            bot.send_message(message.from_user.id, vera_url)
    if message.text.lower() == 'hh':
        time.sleep(2)
        for article_sort in articles_all:
            article_sort_url = article_sort.find("a", class_="bloko-link").get("href")


            bot.send_message(message.from_user.id, article_sort_url)

bot.polling(none_stop=True)