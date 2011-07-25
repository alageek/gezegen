from datetime import datetime
from time import mktime
from lib import feedparser
from lib.utils import get_config
from models.home import Feed


class UpdateFeeds:

    def __init__(self):
        self.config = get_config()

        self.run()

    def delete_old_feeds(self):
        for f in Feed.all():
            f.delete()

    def run(self):
        self.delete_old_feeds()

        for subscription in self.config['subscriptions']:
            result = feedparser.parse(subscription['feed_url'])

            for entry in result.entries:
                date = datetime.fromtimestamp(mktime(entry.updated_parsed))
                feed = Feed(
                    author=subscription['name'],
                    title=entry.title,
                    date=date,
                    content=entry.summary,
                    url = entry.link
                )
                feed.put()

if __name__ == '__main__':
    UpdateFeeds()
