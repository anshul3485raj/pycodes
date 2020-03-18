import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.flipkart.com/search?q=mechanical+keyboard&sid=4rr%2Ckm5%2Cr39&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_3_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mechanical+keyboard|Gaming+Controllers&requestId=455e6b71-22dd-4e71-8dc9-5459c432cfda&as-backfill=on"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

page = requests.get(URL, headers=headers)

soup = bs(page.content, "html.parser")

links = soup.findAll('a')

print(links)