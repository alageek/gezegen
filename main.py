from google.appengine.ext import db
from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp import util
from lib.views import TemplateView

class MainHandler(TemplateView):

    template_name = 'home/index'

    def get_template_values(self):
        template_values = {
            'welcome': 'Welcome, user.'
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
