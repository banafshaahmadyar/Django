from django.urls import path
from admins import views

urlpatterns = [
    path('admins/', views.AdminList.as_view()),
    path('admins/<int:pk>/', views.AdminDetail.as_view()),
]