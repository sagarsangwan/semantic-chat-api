import os

from api.settings.base_settings import BASE_DIR


DEBUG = True
ALLOWED_HOSTS = [
    ".vercel.app",
    "code-chatroom.vercel.app",
    "iamsagarsangwan.pythonanywhere.com",
]

CORS_ALLOWED_ORIGINS = [
    "https://code-chatroom.vercel.app",
]


STATIC_URL = "/static/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
print("sagar-------------------------------")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")
