import requests
from bs4 import BeautifulSoup

URL = 'https://hh.ru/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0',
           'Accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='bloko-link bloko-link_list HH-LinkModifier')
    # Создаем словарь, в котором будем хранить наш результат запроса
    vacancy = []
    for item in items:
        vacancy.append({
            'Vacancy': item.find('span', class_='vacancy-of-the-day__title').get_text(),
            'Wage': item.find('span', class_='vacancy-of-the-day__salary').get_text().replace("\xa0", " ")
            # Убираем неразрывный пробел, представленный в виде "\xa0"
        })
    print(vacancy)
    print('Total vacancies for today: ' + str(len(vacancy)))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Something went wrong')


parse()
