from bs4 import BeautifulSoup
import urllib.request


class Parser:
    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, "html.parser")

    def parsing(self):
        news = self.html.find_all('li', class_='b-news-list__item')
        for item in news:
            title = item.find('a', class_='b-news-list__title').get_text()
            # print(title)
            link = item.a.get('href')
            # print(link)
            news_date = item.find('a', class_='b-news-list__date').get_text()
            # print(news_date)
            self.results.append({
                'title': title,
                'link': link,
                'news_time': news_date
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость №{i}\n\nНазвание: {item["title"]}\nДата новости: {item["news_time"]}\n'
                        f'Ссылка: https://www.f1news.ru{item["link"]}\n\n**********************************************\n\n')
                i += 1
            f.close()

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
        print('Done')
