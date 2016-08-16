from django.conf.urls import include, url
from rest_framework import routers

from .views import AdopterViewSet, ImageViewSet, UserView

router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
router.register(r'user', UserView, 'user')
router.register(r'adopters', AdopterViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

