# To find all the links of any given website

# importing module
import urllib2
import re

# url
url = "www.oceanofgames.com"

# connecting to the url
website  = urllib2.urlopen(url)

# read html code
html = website.read()

# use re.findall to get all the links
links = re.findall("'((http|ftp)s?://.*?)'", html)

print(links)