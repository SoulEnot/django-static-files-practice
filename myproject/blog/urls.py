from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_list_detail, name='post_list_detail'),
    path('new/', views.post_list_create, name='post_list_create'),
]