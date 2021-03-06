from xml.etree.ElementTree import parse
from StringIO import StringIO
import time

import urllib2
import feedparser
import pymongo

import re
import datetime

"""
@TODO: Pake try except untuk handle connection error (timeout)

PIP Source:
Feedparse: http://pythonhosted.org/feedparser/http-etag.html

Mendayagunakan full text search di mongodb dan sukses :)
contoh searching
print db.command('text', 'freewaredata', search='cheatbook freeware download')
"""

import re
from HTMLParser import HTMLParser

whitespace = re.compile('\s+')

class HTMLStripTags(HTMLParser):
    """Strip tags                                                                                                                                                                                                
    """
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.out = ""

    def handle_data(self, data):
        self.out += data

    def handle_entityref(self, name):
        self.out += '&%s;' % name

    def handle_charref(self, name):
        return self.handle_entityref('#' + name)

    def value(self):
        # Collapse whitespace                                                                                                                                                                                    
        return whitespace.sub(' ', self.out).strip()

def plain(html):
    parser = HTMLStripTags()
    parser.feed(html)
    return parser.value()


# pymongo conn dan dbase
c = pymongo.Connection()
db = c['freeware']



while True:
    try:
        url2 = "http://www.softpedia.com/backend.xml"
        xmldata2 = urllib2.urlopen(url2).read()
        data2 = parse(StringIO(xmldata2))            
        date2 = feedparser.parse(url2)
        
        for elem in data2.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date2.feed['updated']
                        })
    except:
        pass

    try:
        url22 = "http://mac.softpedia.com/backend.xml"
        xmldata22 = urllib2.urlopen(url22).read()
        data22 = parse(StringIO(xmldata22))            
        date22 = feedparser.parse(url22)
        
        for elem in data22.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date2.feed['updated']
                        })
    except:
        pass

    try:
        url25 = "http://drivers.softpedia.com/backend.xml"
        xmldata25 = urllib2.urlopen(url25).read()
        data25 = parse(StringIO(xmldata25))            
        date25 = feedparser.parse(url25)
        
        for elem in data25.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date25.feed['updated']
                        })
    except:
        pass

    try:
        url26 = "http://games.softpedia.com/backend.xml"
        xmldata26 = urllib2.urlopen(url26).read()
        data26 = parse(StringIO(xmldata26))            
        date26 = feedparser.parse(url26)
        
        for elem in data26.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date26.feed['updated']
                        })
    except:
        pass

    try:
        url27 = "http://linux.softpedia.com/backend.xml"
        xmldata27 = urllib2.urlopen(url27).read()
        data27 = parse(StringIO(xmldata27))            
        date27 = feedparser.parse(url27)
        
        for elem in data27.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date27.feed['updated']
                        })
    except:
        pass

    try:
        url28 = "http://handheld.softpedia.com/backend-software.xml"
        xmldata28 = urllib2.urlopen(url28).read()
        data28 = parse(StringIO(xmldata28))            
        date28 = feedparser.parse(url28)
        
        for elem in data28.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date28.feed['updated']
                        })
    except:
        pass

    try:
        url29 = "http://webscripts.softpedia.com/backend.xml"
        xmldata29 = urllib2.urlopen(url29).read()
        data29 = parse(StringIO(xmldata29))            
        date29 = feedparser.parse(url29)
        
        for elem in data29.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': elem.find('description').text, 
                        'link': elem.find('link').text,
                        'update': date29.feed['updated']
                        })
    except:
        pass

    try:
        data30 = feedparser.parse("http://feeds.feedburner.com/filecluster")

        for elem in data30['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': plain(elem['summary']),
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        url1 = "http://www.freewarefiles.com/rss/newfiles.xml"
        data1 = feedparser.parse(url1)
        
        for elem in data1['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'], 
                        'description': elem['description'], 
                        'link': elem['link'],
                        'category': elem['category'],
                        'update': data1['updated']
                        })
    except:
        pass
            

    try:
        url3 = "http://feeds.feedburner.com/filehippo?format=xml"
        xmldata3 = urllib2.urlopen(url3).read()
        data3 = feedparser.parse(url3)
        
        for elem in data3['entries']:
            if not db.freewaredata.find_one({'link': elem['id']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        url4 = "http://www.snapfiles.com/feeds/snapfiles.xml"
        xmldata4 = urllib2.urlopen(url4).read()
        data4 = parse(StringIO(xmldata4))
        date4 = feedparser.parse(url4)
        
        for elem in data4.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text,
                        'description': elem.find('description').text,
                        'link': elem.find('link').text,
                        'update': date4['updated']
                        })
    except:
        pass

    try:
        url5 = "http://www.snapfiles.com/feeds/sf20fw.xml"
        xmldata5 = urllib2.urlopen(url5).read()
        data5 = parse(StringIO(xmldata5))
        date5 = feedparser.parse(url5)
        
        for elem in data5.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text,
                        'description': elem.find('description').text,
                        'link': elem.find('link').text,
                        'update': date5['updated']
                        })
    except:
        pass

    try:
        url6 = "http://freewarehome.com/fh.xml"
        xmldata6 = urllib2.urlopen(url6).read()
        data6 = parse(StringIO(xmldata6))
        date6 = feedparser.parse(url6)
        
        for elem in data6.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text,
                        'description': elem.find('description').text,
                        'link': elem.find('link').text,
                        'update': elem.find('pubDate').text
                        })
    except:
        pass

    try:
        url7 = "http://feeds.feedburner.com/pfc"
        xmldata7 = urllib2.urlopen(url7).read()
        data7 = feedparser.parse(url7)
        
        for elem in data7['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': plain(elem['summary']),
                        'link': elem['link'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        url8 = "http://www.majorgeeks.com/files/rss"
        xmldata8 = urllib2.urlopen(url8).read()
        data8 = parse(StringIO(xmldata8))
        date8 = feedparser.parse(url8)
        
        for elem in data8.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text,
                        'description': elem.find('description').text,
                        'link': elem.find('link').text,
                        'update': elem.find('pubDate').text
                        })
    except:
        pass


    # itunes bang
    # 1. 300 new ios applications

    try:
        data9 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/newapplications/limit=300/xml"))

        for elem in data9['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass


    try:
        # 2. 300 top free ios applications
        data10 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topfreeapplications/limit=300/xml"))
        
        for elem in data10['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 3. 300 top paid ios applications
        data11 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/toppaidapplications/limit=300/xml"))

        for elem in data11['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 4. 300 top grossing ios applications
        data12 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topgrossingapplications/limit=300/xml"))
        
        for elem in data12['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 5. 300 top free ipad applications
        data13 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topfreeipadapplications/limit=300/xml"))

        for elem in data13['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 6. 300 top paid ipad applications
        data14 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/toppaidipadapplications/limit=300/xml"))
        
        for elem in data14['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 7. 300 top grossing ipad applications
        data15 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topgrossingipadapplications/limit=300/xml"))
        
        for elem in data15['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'descriptions': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 8. 300 new free ios applications
        data16 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/newfreeapplications/limit=300/xml"))
        
        for elem in data16['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 9. 300 new paid ios applications
        data17 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/newpaidapplications/limit=300/xml"))
        
        for elem in data17['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 10. 300 top mac apps
        data18 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topmacapps/limit=300/xml"))
        
        for elem in data18['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 11. 300 top free mac apps
        data19 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topfreemacapps/limit=300/xml"))
        
        for elem in data19['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 12. 300 top grossing mac apps
        data20 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/topgrossingmacapps/limit=300/xml"))
        
        for elem in data20['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        # 13. 300 top paid mac apps
        data21 = feedparser.parse(urllib2.urlopen("https://itunes.apple.com/us/rss/toppaidmacapps/limit=300/xml"))
        
        for elem in data21['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['id'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        url23 = "http://feeds.feedburner.com/androidzoom/LastGamesAndApplications"
        xmldata23 = urllib2.urlopen(url23).read()
        data23 = feedparser.parse(url23)
        
        for elem in data23['entries']:
            if not db.freewaredata.find_one({'title': elem['title']}):
                db.freewaredata.insert({
                        'title': elem['title'],
                        'description': elem['summary'],
                        'link': elem['feedburner_origlink'],
                        'update': elem['updated']
                        })
    except:
        pass

    try:
        url24 = "http://www.appbrain.com/rss/browse/apps/?apps=latest"
        xmldata24 = urllib2.urlopen(url24).read()
        data24 = parse(StringIO(xmldata24))            
        # date24 = feedparser.parse(url24)
        
        for elem in data24.getroot().iter('item'):
            if not db.freewaredata.find_one({'title': elem.find('title').text}):
                db.freewaredata.insert({
                        'title': elem.find('title').text, 
                        'description': plain(elem.find('description').text), 
                        'link': elem.find('link').text,
                        'update': elem.find('pubDate').text
                        })
    except:
        pass

    try:
        data31 = feedparser.parse("http://www.userdrivers.com/rss.xml")
        
        for elem in data31['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': elem.description,
                        'link': elem.link,
                        'update': elem.published,
                        'category': elem.category
                        })
    except:
        pass

    try:
        data32 = feedparser.parse("http://rss.afterdawn.com/software_updates.xml")
        
        for elem in data32['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': elem.summary,
                        'link': elem.link,
                        'update': data32.updated,
                        })
    except:
        pass

    try:
        data33 = feedparser.parse("http://filedir.com/rss/windows/")
        
        for elem in data33['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': plain(elem.description),
                        'category': elem.category,
                        'link': elem.link,
                        'update': elem.published,
                        })
    except:
        pass

    try:
        data34 = feedparser.parse("http://filedir.com/rss/mac-os/")
        
        for elem in data34['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': plain(elem.description),
                        'category': elem.category,
                        'link': elem.link,
                        'update': elem.published,
                        })
    except:
        pass

    try:
        data35 = feedparser.parse("http://filedir.com/rss/windows-games/")
        
        for elem in data35['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': plain(elem.description),
                        'category': elem.category,
                        'link': elem.link,
                        'update': elem.published,
                        })
    except:
        pass

    try:
        data36 = feedparser.parse("http://filedir.com/rss/linux/")
        
        for elem in data36['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': plain(elem.description),
                        'category': elem.category,
                        'link': elem.link,
                        'update': elem.published,
                        })
    except:
        pass

    try:
        data37 = feedparser.parse("http://filedir.com/rss/mac-os-games/")
        
        for elem in data37['entries']:
            if not db.freewaredata.find_one({'title': elem.title}):
                db.freewaredata.insert({
                        'title': elem.title,
                        'description': plain(elem.description),
                        'category': elem.category,
                        'link': elem.link,
                        'update': elem.published,
                        })
    except:
        pass

# dari filedir yang belum:
# android apps, android games, iphone apps, iphone games, winmo apps, winmo games

    # brothersoft scraping :evil:

    try:
        titles = [i for i in re.findall(re.compile(r"aimpT\"><a href=\"/.*\.html\">(.*?)</a>", re.MULTILINE), urllib2.urlopen("http://www.brothersoft.com/windows/new-update/").read()) if i != 'Last']
        descriptions = [i for i in re.findall(re.compile(r"anti\">(.*?)</td>"), urllib2.urlopen("http://www.brothersoft.com/windows/new-update/").read()) if i != 'Last']
        urls = ["http://www.brothersoft.com" + i for i in re.findall(re.compile(r"<a href=\"(.*\.html).*\">Download Now</a>"), urllib2.urlopen("http://www.brothersoft.com/windows/new-update/").read()) if i != 'Last']

        if (len(titles) == len(descriptions) == len(urls)) and len(titles) > 1:
            for i in range(len(titles)):
                if not db.freewaredata.find_one({'title': titles[i]}):
                    db.freewaredata.insert({
                            'title': titles[i],
                            'description': descriptions[i],
                            'link': urls[i],
                            'update': datetime.datetime.now()
                            })
    except:
        pass

    # print len([i for i in db.freewaredata.find()])
    time.sleep(300)
