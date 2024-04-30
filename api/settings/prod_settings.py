import dj_database_url
import os

from api.ss import BASE_DIR


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", "now.sh"]

STATIC_URL = "static/"
SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
DATABASES = {
    "ENGINE": "django.db.backends.postgresql",
    "default": dj_database_url.config(default=SUPABASE_DB_URL, conn_max_age=600),
}

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
