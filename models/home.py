from google.appengine.ext import db


class Subscription(db.Model):
    name = db.StringProperty()
    url = db.URLProperty()
    feed_url = db.URLProperty()
    avatar_url = db.URLProperty(required=False)
    email = db.EmailProperty()
    is_active = db.BooleanProperty()
    date = db.DateTimeProperty(auto_now_add=True)
