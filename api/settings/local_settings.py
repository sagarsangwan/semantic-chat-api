from api.settings import BASE_DIR


DEBUG = True

# ALLOWED_HOSTS = []

STATIC_URL = "static/"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    # "localhost",
    "http://127.0.0.1:3000",
]
ALLOWED_HOSTS = ["127.0.0.1", "localhost:8000", "http://127.0.0.1:8000"]
