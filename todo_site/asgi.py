"""
asgi.py
Tento soubor slouží jako vstupní bod pro ASGI (Asynchronous Server Gateway Interface),
což je standard rozhraní mezi webovými servery a asynchronními aplikacemi v Pythonu.

Je potřebný pro podporu asynchronních operací a WebSocketů
(protokol umožňující obousměrnou komunikaci mezi klientem a serverem v reálném čase) v Djangu.
"""

"""
ASGI config for todo_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_site.settings')

application = get_asgi_application()
