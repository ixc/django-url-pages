from django.template import TemplateDoesNotExist, loader
from django.template.response import TemplateResponse


class URLPageMiddleware(object):
    def process_request(self, request, *args, **kwargs):
        """
        Return a ``TemplateResponse`` for the requested URL path.

        Template names will be matched exactly, or with a ``.html`` or
        ``/index.html`` suffix, and a ``django-url-pages`` prefix.
        """
        path = request.path.lstrip('/')
        template_names = [
            'django-url-pages/%s' % path,
            'django-url-pages/%s.html' % path.rstrip('/'),
            'django-url-pages/%s/index.html' % path.rstrip('/'),
        ]
        try:
            template = loader.select_template(template_names)
        except TemplateDoesNotExist:
            return None
        else:
            return TemplateResponse(request, template)
