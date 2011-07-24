from google.appengine.ext import db
from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp import util
from lib.views import TemplateView
from lib.utils import get_config


class MainHandler(TemplateView):

    template_name = 'home/index'

    def get_template_values(self):
        subscriptions = get_config().get('subscriptions')
        template_values = {
            'welcome': 'Welcome, user.',
            'subscriptions': subscriptions
        }

        return template_values


def main():
    application = WSGIApplication(
        [('/', MainHandler)],
        debug=True
    )

    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
