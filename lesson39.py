from bs4 import BeautifulSoup
# import request
import urllib.request

req = urllib.request.urlopen('https://www.f1news.ru/')
html = req.read()
# request.link
# print(request.link)

soap = BeautifulSoup(html, "html.parser")
news = soap.find_all('li', class_='b-news-list__item')

results = []
for item in news:
    title = item.find('a', class_='b-news-list__title').get_text()
    # print(title)
    link = item.a.get('href')
    # print(link)
    news_date = item.find('a', class_='b-news-list__date').get_text()
    # print(news_date)
    results.append({
        'title': title,
        'link': link,
        'news_time': news_date
    })
f = open('f-1news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость №{i}\n\nНазвание: {item["title"]}\nДата новости: {item["news_time"]}\n'
            f'Ссылка: https://www.f1news.ru{item["link"]}\n\n******************************************\n\n')
    i += 1
f.close()
print('Done')
# print(f'{results}\n')
