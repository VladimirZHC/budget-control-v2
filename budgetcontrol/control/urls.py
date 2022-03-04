from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'operations', views.OperationViewSet)
router.register(r'tags', views.TagViewSet)


urlpatterns = [
    path('', include(router.urls))
]