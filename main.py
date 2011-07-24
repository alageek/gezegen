import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

class TemplateView(webapp.RequestHandler):

    template_name = None
    template_path = os.path.join(os.path.dirname(__file__), 'views')

    def get_template(self):
        try:
            return os.path.join(self.template_path, '%s.html' % self.template_name)
        except AttributeError:
            return None

    def get_template_values(self):
        return {}

    def get(self):
        context = template.render(self.get_template(), self.get_template_values())

        self.response.out.write(context)


class MainHandler(TemplateView):

    template_name = 'home/index'

    def get_template_values(self):
        template_values = {
            'welcome': 'Welcome, user.'
        }

        return template_values


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
