import os

from api.settings.base_settings import BASE_DIR


DEBUG = True
ALLOWED_HOSTS = [
    ".vercel.app",
    "semantic-chat-api.vercel.app",
    ".now.sh",
    "127.0.0.1",
    "iamsagarsangwan.pythonanywhere.com",
]
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
