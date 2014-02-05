"""
@TODO: Bagaimana cara mengetahui konten sudah diupdate atau belum?
Pertama search apakah ada data dengan update tanggal sama
Jika ada, gak usah update, otherwise update

PIP Source:
Feedparse: http://pythonhosted.org/feedparser/http-etag.html

Mendayagunakan full text search di mongodb dan sukses :)
"""

import urllib2
from xml.etree.ElementTree import parse
from StringIO import StringIO
import feedparser
import pymongo
from pprint import pprint

# pymongo conn dan dbase
c = pymongo.Connection()
db = c['freeware']

url1 = "http://www.freewarefiles.com/rss/newfiles.xml"
xmldata1 = urllib2.urlopen(url1).read()
data1 = parse(StringIO(xmldata1))
date1 = feedparser.parse(url1)

# d1.modified # key1 (tanggal terakhir / terbaru)
# d2.feed['updated'] # key2 (tanggal terakhir / terbaru)

db.freewaredata.remove()

if not db.freewaredata.find_one({'update': date1.modified}):
    for elem in data1.getroot().iter('item'):
        # print elem.find('title').text
        # print elem.find('description').text
        db.freewaredata.insert({'title': elem.find('title').text, 'description': '<b> ' + elem.find('title').text + ' </b> ' + elem.find('description').text, 'update': date1.modified})

url2 = "http://www.softpedia.com/backend.xml"
xmldata2 = urllib2.urlopen(url2).read()
data2 = parse(StringIO(xmldata2))
date2 = feedparser.parse(url2)

if not db.freewaredata.find_one({'update': date2.feed['updated']}):
    for elem in data2.getroot().iter('item'):
        # print elem.find('title').text
        # print elem.find('description').text
        db.freewaredata.insert({'title': elem.find('title').text, 'description': '<b> ' + elem.find('title').text + ' </b> ' + elem.find('description').text, 'update': date2.feed['updated']})

print db.command('text', 'freewaredata', search='cheatbook freeware sex download')
