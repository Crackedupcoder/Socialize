from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.post_like, name='like'),
    path('post/add/', views.post_create, name='add-post'),
]