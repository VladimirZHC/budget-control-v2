from django.urls import path
from control import views

urlpatterns = [
    path('operations/', views.operation_list),
    path('operations/<int:pk>/', views.operation_detail),
]