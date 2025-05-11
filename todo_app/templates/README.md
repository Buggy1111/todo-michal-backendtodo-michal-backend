# templates/
Tato složka obsahuje HTML šablony používané v aplikaci.
Šablony jsou soubory, které slouží k vykreslování dynamického obsahu na webové stránce.
Můžeme zde používat Django templating language, který umožňuje vkládání proměnných, vykonávání podmínek a cyklů.
Každá aplikace může mít vlastní složku templates, nebo můžeme použít globální složku na úrovni projektu.
Django automaticky hledá šablony ve složce 'templates' každé aplikace, pokud je 'APP_DIRS' (v souboru settings.py) v nastavení povoleno.
