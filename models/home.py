from google.appengine.ext import db


class Feed(db.Model):
    author = db.StringProperty()
    title = db.StringProperty()
    date = db.DateTimeProperty()
    content = db.TextProperty()
    url = db.URLProperty()
