from django.urls import path
from control import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('operations/', views.operation_list),
    path('operations/<int:pk>/', views.operation_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)