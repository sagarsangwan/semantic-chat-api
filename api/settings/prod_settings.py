import os

from api.settings.base_settings import BASE_DIR


DEBUG = True
ALLOWED_HOSTS = [".vercel.app", "sagarsangwan.vercel.app", ".now.sh"]
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles_build", "static")
#
STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
print("sagar-------------------------------")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Configures the staticfiles directory to serve
# static files from /static/ on our deployment
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": os.environ.get("HOST"),
        "NAME": os.environ.get("NAME"),
        "USER": os.environ.get("USER"),
        "PASSWORD": os.environ.get("PASSWORD"),
        "PORT": os.environ.get("PORT"),
    }
}
# import dj_database_url

# SUPABASE_DB_URL = os.environ.get("SUPABASE_DB_URL")
# DATABASES = {
#     "default": dj_database_url.config(default=SUPABASE_DB_URL, conn_max_age=600)
# }
