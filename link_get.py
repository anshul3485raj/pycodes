# python program to list down all mechanical keboard

# importing module
import requests
from bs4 import BeautifulSoup

URL = "https://www.google.com/search?safe=active&sxsrf=ALeKk02gWtyeVTtHlaTebVKcC5CPfGVMKw%3A1583989216441&source=hp&ei=4MFpXvmtGNOortoPwuit0AY&q=udemy&oq=ude&gs_l=psy-ab.3.0.35i39j0l4j0i131j0l4.169569.170207..172000...2.0..0.142.403.0j3......0....1..gws-wiz.....10..35i362i39.6sXXkP89vQQ"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

link = soup.findAll('a')

print(link)

      