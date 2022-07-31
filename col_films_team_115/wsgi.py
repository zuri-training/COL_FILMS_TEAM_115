"""
WSGI config for col_films_team_115 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# ADDED
from static_ranges import Ranges
from dj_static import Cling, MediaCling
# END ADDED 
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'col_films_team_115.settings')

# application = get_wsgi_application()
application = Ranges(Cling(MediaCling(get_wsgi_application())))
