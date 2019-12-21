"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.


dataset_3378_3.txt

"""
import requests

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"
file = "699991.txt"
url = base_url + file

while requests.get(url).text[:2] != "We":
    file = requests.get(url).text
    url = base_url + file

print(requests.get(url).text)

"""
====================================================

import requests

base_url = "https://stepic.org/media/attachments/course67/3.6.3/"
file = "699991.txt"
s = ""

while True:
    url = base_url + file
    r = requests.get(url)

    if r.text.count("We") >= 1:
        s = r.text
        break
    else:
        file = r.text

print(s)
====================================================

import requests
urlname = "https://stepic.org/media/attachments/course67/3.6.3/"
filename= "699991.txt"

r = requests.get(urlname + filename)

while True:
    words = r.text.split()
    if words[0]=="We":
        print(r.text)
        break
    else:
        filename =r.text
        r = requests.get(urlname + filename)

====================================================

import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get(url + "699991.txt")

while not r.text.startswith("We"):
    r = requests.get(url + r.text)
    print(r.text)

print(r.text)

====================================================

import requests
url, name = 'https://stepic.org/media/attachments/course67/3.6.3/', '699991.txt'

while name[:2] != 'We':
    name = requests.get(url + name).text

print(name)

====================================================

"""