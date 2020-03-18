# Python program to scrape data from websites

# importing modules
from selenium import webdriver # selenium
from bs4 import BeautifulSoup # BeautifulSoup
import pandas as pd # pandas
import requests # requests

# URL of the webpage
URL = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

# headers (Mozilla webdriver)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

# request to the webpage
page = requests.get(URL, headers=headers)

# soup to parse the data 
soup = BeautifulSoup(page) # html content

for a in soup(len(page)):
    name = a.find('title', attrs={"class":"_2cLu-l"})
    price = a.find('div', attrs={"class":"_1vC4OE"})
    rating = a.find('div', attrs={"class":"VGWI6T"})
    products.append(name)
    prices.append(price)
    ratings.append(rating)

print("Name : ", products )
print("Price : ", prices)
print("ratings : ", rating)


df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')

