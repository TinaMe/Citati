from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

import random

MAIN_URL = "http://quotes.yourdictionary.com/theme/marriage/"

webpage = urlopen(MAIN_URL).read()

nice_webpage = BeautifulSoup(webpage)


citat = nice_webpage.findAll("p", {"class": "quoteContent"})


for i in range(5):
    stevilka_citata = random.randint(0, len(citat)-1-i)
    print citat[stevilka_citata].string.strip()
    citat.pop(stevilka_citata)




