"""
manage.py
Tento soubor slouží jako rozhraní pro správu Django projektu.
Umožňuje spouštět různé příkazy jako spuštění serveru, migrace databáze, tvorba aplikací, atd.
Příkazy spouštíme pomocí 'python manage.py <příkaz>'.
"""

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
