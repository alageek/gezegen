from google.appengine.ext import db


class Feed(db.Model):
    author = db.StringProperty()
    title = db.StringProperty()
    content = db.TextProperty()
    url = db.URLProperty()
    date = db.DateTimeProperty()
