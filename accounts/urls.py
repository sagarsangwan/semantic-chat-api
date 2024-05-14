from django.urls import path
from .views import UserDetailViewsets
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users", UserDetailViewsets)


urlpatterns = router.urls
