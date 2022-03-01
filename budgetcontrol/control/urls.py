from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'operations', views.OperationViewSet)


urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('operations/', views.OperationList.as_view()),
#     path('operations/<int:pk>/', views.OperationDetail.as_view()),
#     path('', views.api_root),
#     path('operations/<int:pk>/highlight/', views.OperationHighlight.as_view())
# ]

# urlpatterns = format_suffix_patterns([
#     path('', views.api_root),
#     path('operations/', views.OperationList.as_view(), name='operation-list'),
#     path('operations/<int:pk>/', views.OperationDetail.as_view(), name='operation-detail'),
#     path('operations/<int:pk>/highlight/', views.OperationHighlight.as_view(), name='operation-highlight')
# ])

