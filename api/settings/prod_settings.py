import dj_database_url
import os


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app", "now.sh"]

STATIC_URL = "static/"
SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
DATABASES = {
    "default": dj_database_url.config(default=SUPABASE_DB_URL, conn_max_age=600)
}
