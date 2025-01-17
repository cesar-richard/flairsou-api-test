# flake8: noqa
# (on laisse le commentaire pour la génération de la clef dépasser)

# Configurations du serveur - template
# Ce fichier doit être copié sous le nom config.py dans le répertoire flairsou
# LE FICHIER config.py NE DOIT PAS ETRE COMMIT
from pathlib import Path

# répertoire de base, nécessaire pour la database par défaut
BASE_DIR = Path(__file__).resolve().parent.parent

# clé secrète - à remplacer
# on peut générer une clé avec la commande suivante
# (exécutée depuis la racine du projet) :
# python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
SECRET_KEY = "<SECRET_KEY>"

# activation du debug ou non
DEBUG = True

# timezone
TIME_ZONE = "UTC"

# database config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ALLOWED_HOSTS = []

UPLOAD_PATH = "uploads/"

OAUTH_SETTINGS = {
    "client_id": "xxxxxxx",
    "client_secret": "xxxxxxx",
    "authorization_url": "https://assos.utc.fr/oauth/authorize",
    "token_url": "https://assos.utc.fr/oauth/token",
    "redirect_uri": "http://xxxxxxxxx",
    "api_base_url": "https://assos.utc.fr/api/v1",
    "scopes": [
        "user-get-info",
        "user-get-roles",
        "user-get-assos",
    ],
    "login_redirect": "/",
    "logout_redirect": "/",
}
