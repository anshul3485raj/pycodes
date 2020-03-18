# python program to extract all links from website

# importing modules
import requests
import re

def find_links(page_source):
    regex = re.compile("<a title=",">")
    result = regex.findAll(page_source)
    return result

res = requests.get('https://www.flipkart.com/search?q=mechanical+keyboard&sid=4rr%2Ckm5%2Cr39&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_3_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mechanical+keyboard|Gaming+Controllers&requestId=455e6b71-22dd-4e71-8dc9-5459c432cfda&as-backfill=on')

links = find_links(res.text)

for i in range(len(regex)):
    print(links)