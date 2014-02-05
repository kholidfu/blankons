from flask import render_template, request, redirect, send_from_directory, make_response
from werkzeug.contrib.atom import AtomFeed # feed
from app import app
from filters import slugify, splitter, onlychars, get_first_part, get_last_part

import urllib
import pymongo
from bson.objectid import ObjectId
import random
import datetime
import redis
import cPickle

@app.template_filter()
def getlast(text, delim=' '):
  return get_last_part(text, delim)

@app.template_filter()
def getfirst(text, delim=' '):
  return get_first_part(text, delim)

# fungsi: mengubah sentence menjadi slug
# usage: {{ title|slug }}
@app.template_filter()
def slug(s):
  return slugify(s)

# split s with delim '-'
# usage: {{ string|split }}
# returns list
@app.template_filter()
def split(s, delim='-'):
  return splitter(s, delim)

@app.template_filter()
def getchars(text):
  """get characters and numbers only from string"""
  return onlychars(text)

# handle robots.txt file
@app.route("/robots.txt")
def robots():
  return send_from_directory(app.static_folder, request.path[1:])

# pymongo conn dan dbase
c = pymongo.Connection()
db = c['freeware']
dbsetem = c['setem']

r = redis.Redis()

# sorting pymongo descending (last masuk keluar duluan)
# dbsetem.ptfsetem.find().sort("_id", -1).limit(5)

@app.route("/")
def index():
  # jumlah data
  numfree = db.freewaredata.find().count()
  num = dbsetem.ptfsetem.find().count()

  # cache latest data
  if len(r.lrange('freewaredata', 0, -1)) > 0:
    data = [cPickle.loads(i) for i in (r.lrange('freewaredata', 0, -1))]
  else:
    [r.rpush('freewaredata', cPickle.dumps(i)) for i in db.freewaredata.find().sort("_id", -1).limit(10)]
    r.expire('freewaredata', 1800)
    data = [cPickle.loads(i) for i in (r.lrange('freewaredata', 0, -1))]

  # cache setem
  if len(r.lrange('setem', 0, -1)) > 0:
    queries = r.lrange('setem', 0, -1)
  else:
    num = dbsetem.ptfsetem.find().count()
    queries = [r.rpush('setem', i['q']) for i in dbsetem.ptfsetem.find().skip(random.randint(0, int(num))).limit(25)]
    r.expire('setem', 1800)

  return render_template("index.html", data=data, queries=queries, num=num, numfree=numfree)

@app.route("/c")
def redirect_search():
  q = request.args.get('q')
  return redirect("/" + slugify(q), 301)

@app.route("/<q>/<file_id>")
def search(q, file_id):
  title = db.freewaredata.find_one({'_id': ObjectId(file_id)})
  results = db.command('text', 'freewaredata', search=q, limit=10)
  num = dbsetem.ptfsetem.find().count()
  numfree = db.freewaredata.find().count()
  queries = [i for i in dbsetem.ptfsetem.find().skip(random.randint(0, int(num))).limit(25)]
  return render_template("search.html", results=results, q=q, queries=queries, num=num, numfree=numfree, title=title)

@app.route("/<q>")
def setem(q):
  if q != 'favicon.ico':
    dbsetem.ptfsetem.insert({'q': q})
  results = db.command('text', 'freewaredata', search=q, limit=10)
  num = dbsetem.ptfsetem.find().count()
  numfree = db.freewaredata.find().count()
  queries = [i for i in dbsetem.ptfsetem.find().skip(random.randint(0, int(num))).limit(25)]
  return render_template("setem.html", q=q, results=results, queries=queries, num=num, numfree=numfree)

@app.route("/get/<file_id>")
def get_url(file_id):
  data = db.freewaredata.find_one({'_id': ObjectId(file_id)})
  return render_template("download.html", data=data)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/sitemap/<n>")
def sitemap(n):
  start = (int(n) * 50000) - 50000
  end = (int(n) * 50000)
  data = db.freewaredata.find()[start:end]
  sitemap_xml = render_template("sitemap.xml", data=data)
  response = make_response(sitemap_xml)
  response.headers['Content-Type'] = 'application/xml'

  return response

#@app.route("/sitemap-<n>.xml")
#def sitemapd(n):
#  start = int(n) * 50000
#  data = db.freewaredata.find()[start:]
#  sitemap_xml = render_template("sitemap2.xml", data=data)
#  response = make_response(sitemap_xml)
#  response.headers['Content-Type'] = 'application/xml'
#
#  return response

@app.route('/latest.atom')
def recent_feed():
  # http://werkzeug.pocoo.org/docs/contrib/atom/                                                                                                                                                               
  feed = AtomFeed('Recent Files',
                  feed_url = request.url, url=request.url_root)
  data = db.freewaredata.find().sort("_id", -1).limit(100)
  for d in data:
    try:
      feed.add(
        d['title'],
        d['description'],
        content_type='text', 
        id=d['_id'],
        url='http://www.blankons.com/'+slugify(onlychars(d['title']))+'/'+unicode(d['_id']),
        updated=datetime.datetime.now(),
        )
    except:
      feed.add(
        d['title'],
        content_type='text', 
        id=d['_id'],
        url='http://www.blankons.com/'+slugify(onlychars(d['title']))+'/'+unicode(d['_id']),
        updated=datetime.datetime.now(),
        )
  return feed.get_response()
  
# ini tambahan dari emacs tramp mode
