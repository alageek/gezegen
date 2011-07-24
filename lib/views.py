import os
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp import template


class TemplateView(RequestHandler):

    template_name = None
    template_path = os.path.join(os.path.dirname(__file__), '..', 'views')

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
