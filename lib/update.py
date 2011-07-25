import feedparser
from datetime import datetime
from time import mktime
from lib.utils import get_config
from models.home import Feed


class UpdateFeeds:

    def __init__(self):
        self.config = get_config()

        self.run()


    def run(self):
        for subscription in self.config['subscriptions']:
            result = feedparser.parse(subscription['feed_url'])

            for entry in result.entries:
                date = datetime.fromtimestamp(mktime(entry.updated_parsed))
                feed = Feed(
                    author=subscription['name'],
                    title=entry.title,
                    date=date,
                    url = entry.link
                )
                feed.put()

if __name__ == '__main__':
    UpdateFeeds()
