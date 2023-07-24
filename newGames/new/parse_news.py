from urllib.request import Request, urlopen
import requests
import bs4
import json

URL = 'https://media.vkplay.ru/news/'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.0.2534 Yowser/2.5 Safari/537.36',
            'Content-Type': 'text/html; charset=utf-8',
           # "Content-Type": "application/json"
           }

import time
import threading

delay = 300 #время между вызовами функции в секундах


def parse_new(): #вызываемая в отдельном потоке функция в ней и производим действия из следующего шага
    url = "https://epic-games-store.p.rapidapi.com/getNews/locale/ru/limit/30"
    headers = {
        "X-RapidAPI-Key": "40bd4948c6msh348b642de211f5ep11761ejsne02517a39cb7",
        "X-RapidAPI-Host": "epic-games-store.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    print(response.json())


while True:
    thread = threading.Thread(target=parse_new())
    thread.start()
    time.sleep(delay)

#
#
# def check_film(link):
#     req = Request(link, headers=HEADERS)
#     webpage = urlopen(req).read().decode("utf8")
#     html = bs4.BeautifulSoup(webpage, 'html.parser')
#
#     flists = html.select('.full > script')
#     for obj in flists:
#         try:
#             gen = []
#             json_obj = json.loads(obj.text)
#             desc = json_obj['description']
#             name = json_obj['name']
#             url_film = json_obj['url']
#             img = json_obj['thumbnailUrl']
#             upload_date = json_obj['uploadDate']
#             date_published = json_obj['datePublished']
#             genre = json_obj['genre']
#             genre_list = genre.split(', ')
#             for obj in genre_list:
#                 gen.append(obj)
#             embed_url = json_obj['embedUrl']
#         except:
#             continue
#     context = {
#         'name': name,
#         'desc': desc,
#         'img': img,
#         'url': url_film,
#         'upload_date': upload_date,
#         'date_published': date_published,
#         'genre': gen,
#         'embed_url': embed_url,
#     }
#     # save_film(context)
#     return context
#
#
# def check_films(pages):
#     films_list = []
#     for page in range(1, int(pages)):
#         req = Request(URL+'page/'+str(page)+'/', headers=HEADERS)
#         webpage = urlopen(req).read()
#         html = bs4.BeautifulSoup(webpage, 'html.parser')
#         items = html.select('.th-item > a')
#         for item in items:
#             films_list.append(check_film(item['href']))
#         print('page: ', page)
#
#     return films_list
#
#
# def check_page():
#     req = Request(URL, headers=HEADERS)
#     webpage = urlopen(req).read()
#     html = bs4.BeautifulSoup(webpage, 'html.parser')
#     # print(html)
#
#     # print(items)
#     # response = check_films(items)
#     return type(items)
#
#
# s = check_page()
# print(s)
# # print(len(s))
#
# # f = open('list_films.py', 'a')
# # for obj in s:
# #     f.write(str(obj) + '\n')
# # f.write(']')
# # f.close()
