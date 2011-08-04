from datetime import datetime
from time import mktime
from lib import feedparser
from lib.utils import get_config
from models.home import Feed
import logging

class FeedFilter:
    """A class for cleaning up and filtering feeds.
    Fixing datetime etc...
    """

    def get(self, feed_data):
        cleaned_feed_data = self.__fix_dates(feed_data)
        logging.info("%d entries cleaned" % len(cleaned_feed_data))
        return cleaned_feed_data

    def __fix_dates(self, feed_data):
        """
        Fixes that all entries in feed_data has "date" field inside it.
        """
        for entry in feed_data.entries:
            try:
                # Try to get date info from entry
                entry.date = datetime.fromtimestamp(mktime(entry.updated_parse))
                del(entry.updated_parsed)
            except AttributeError:
                # Means that entry has no date info, so we are  getting it from
                # feeds update time.
                entry.date = datetime.fromtimestamp(
                    mktime(feed_data['feed']['updated_parsed']))
        return feed_data

    def __fix_code_blocks(self):
        # may be ha?
        pass

feed_filter = FeedFilter()

class UpdateFeeds:

    def __init__(self):
        self.config = get_config()
        self.run()

    def run(self):
        for subscription in self.config['subscriptions']:
            logging.info("Parsing started for :%s" % subscription['url'])
            # get feed data from subscription
            feed_data = feedparser.parse(subscription['feed_url'])

            # clean it up...
            feed_data = feed_filter.get(feed_data)

            for entry in feed_data.entries:

                # entry becomes a anchestor to entry that stored on
                # database, or returns 0
                entry_on_db = Feed.all().filter("url =", entry.link).get()

                if entry_on_db:

                    # If exists, look for update date,
                    time_difference = entry_on_db.date - entry.date

                    if time_difference.seconds > 0:
                        # It needs to be updated.
                        entry_on_db.title = entry.title
                        entry_on_db.content = entry.summary
                        entry_on_db.date = entry.date
                        entry_on_db.put()
                        logging.info("%s is updated, time difference was %d seconds" % (entry_on_db.url, time_difference.seconds))
                    else:
                        # I now that is not needed but i want that code
                        # easy to read
                        pass
                else:
                    # If not exists , create a new one
                    entry_on_db = Feed(
                        author=subscription['name'],
                        title=entry.title,
                        date=date,
                        content=entry.summary,
                        url=entry.link)
                    # Put it to database ^_^
                    entry_on_db.put()
                    logging.info("%s is added" % entry_on_db.url)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    UpdateFeeds()
