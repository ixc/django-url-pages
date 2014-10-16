Overview
========

Provides a middleware class that returns a `TemplateResponse` for the requested
URL, making it easy for front-end developers to add simple pages to a site and
make use of Django's template language, without messing with views.


Installation
============

Add to your `settings` module:

    MIDDLEWARE_CLASSES += ('django_url_pages.middleware.URLPageMiddleware', )


Usage
=====

Place templates in a `django-url-pages` directory that can be found by an
installed template loader. E.g. a directory referenced in the `TEMPLATE_DIRS`
setting or the `templates` directory for an installed app.


Naming Templates
================

The middleware class will attempt to load templates using the following
template name patterns:

  * `djangosite-url-pages/<url>` (exact match)
  * `djangosite-url-pages/<url>.html` (clean URL for HTML pages)
  * `djangosite-url-pages/<url>/index.html` (default page for directories)
