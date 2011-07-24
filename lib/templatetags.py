from google.appengine.api import images
from google.appengine.ext.webapp.template import create_template_register

register = create_template_register()

def thumbnail(file_path):
    pass

register.filter(thumbnail)
