
DESIRED_HUBS = ['дизайн', 'фото', 'web', 'python']
HEADERS = {'User-Agent':
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'}
from decorator import decor
from decorator_param import decor_param
import requests
from bs4 import BeautifulSoup



@decor_param(param = 'log/some_log.log')
def task(article, DESIRED_HUBS, ):
    for ar in article:
        preview = ar.find(class_ = 'article-formatted-body').find_all('p')
        for prev in preview:
            prev_lower = prev.text.lower()
            if any([prev_lower in desired for desired in DESIRED_HUBS]):
                date = ar.find(class_ = 'tm-article-snippet__datetime-published').find('time')
                title = ar.find(class_ = 'tm-article-snippet__title-link').find('span')
                link = ar.find('a', class_ = 'tm-article-snippet__title-link')
                print(date.attrs.get('datetime'))
                print(title.text)
                print(link.attrs.get('href'))
                print()
                break


if __name__ == '__main__':

    req = requests.get('https://habr.com/ru/all/', headers = HEADERS)
    soup = BeautifulSoup(req.text, 'html.parser')
    article = soup.find_all('article')

    task(article, DESIRED_HUBS)
