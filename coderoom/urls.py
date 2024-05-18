from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CodeRoomViewsets


router = DefaultRouter()
router.register(r"coderoom", CodeRoomViewsets)

urlpatterns = router.urls
