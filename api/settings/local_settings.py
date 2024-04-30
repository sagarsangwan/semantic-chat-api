from api.settings import BASE_DIR


DEBUG = True

# ALLOWED_HOSTS = []

STATIC_URL = "static/"

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
#     "localhost",
# ]
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
