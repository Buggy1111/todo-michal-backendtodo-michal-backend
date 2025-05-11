"""
wsgi.py
Tento soubor slouží jako vstupní bod pro WSGI (Web Server Gateway Interface),
což je standard rozhraní mezi webovými servery a aplikacemi v Pythonu.
Pomáhá s nasazením aplikace na produkční servery.
"""

"""
WSGI config for todo_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_site.settings')

application = get_wsgi_application()
