from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


operation_history = views.OperationHistoryViewSet.as_view(
    {
        'get': 'list',
    }
)


router = DefaultRouter()
router.register(r'operations', views.OperationViewSet)
router.register(r'tags', views.TagViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('operations/<int:pk>/history/', operation_history, name='operation-history'),
]