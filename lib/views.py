from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp import template
from utils import get_path


class TemplateView(RequestHandler):

    template_name = None
    template_path = get_path('views')

    def get_template(self):
        try:
            return '%s/%s.html' % (self.template_path, self.template_name)
        except AttributeError:
            return None

    def get_template_values(self):
        return {}

    def get(self):
        context = template.render(self.get_template(), self.get_template_values())

        self.response.out.write(context)

template.register_template_library('lib.templatetags')
