""" Warning:
Yang most popular download masih ikut ke grab! 
Solusinya: field nya dibikin unik
"""

import requests
import re
import pymongo
import time

c = pymongo.Connection()
db = c['setem']

user_agent = {'User-agent': 'Mozilla/5.0'}
url = 'http://www.ptf.com'

while True:
    html = requests.get(url, headers=user_agent).content
    pattern = "<a href=.*\+.*/\">(.*)</a>"
    found = re.compile(pattern, re.MULTILINE)
    data = re.findall(found, html)

    for d in data:
        if not db.ptfsetem.find_one({'q': d}):
            db.ptfsetem.insert({'q': d})

    # print len([i for i in db.ptfsetem.find()])
    time.sleep(3)
