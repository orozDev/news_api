from rest_framework import routers
from django.urls import path, include
from .yasg import urlpatterns as url_doc
from .views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('news', NewsViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('auth/', include('core.api.auth.urls')),
    path('', include(router.urls)),
]

urlpatterns += url_doc