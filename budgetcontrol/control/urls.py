from django.urls import path
from control import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('operations/', views.OperationList.as_view()),
    path('operations/<int:pk>/', views.OperationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)