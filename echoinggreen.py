import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re
import unicodedata

#write article urls to textfile
all_text = ""


#get contents of Civicist archives
base_url = "http://www.inc.com/bartie-scott/echoing-green-fellows-2016-for-profit-social-entrepreneurship.html"

r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

contents = soup.findAll('div', attrs={"class": "article-body inc_editable"})
for c in contents:
  print c.text.encode('utf-8')





