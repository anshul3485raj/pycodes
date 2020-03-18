
# importing modules
import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

content = soup.findAll("a")

print(content)