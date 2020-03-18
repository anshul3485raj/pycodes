# Python program to scrape data from website

# importing module
import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

content = bs.findAll("h1")
