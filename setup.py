from django_url_pages import __version__
import setuptools

setuptools.setup(
    name='django-url-pages',
    version=__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/django-url-pages',
    license='BSD',
)
