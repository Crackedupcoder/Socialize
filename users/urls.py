from django.urls import path
from .views import SignUpPageView
from . import views

urlpatterns = [
    path('signup/', SignUpPageView.as_view(), name='signup'),
    path('setting/', views.user_update_view, name='setting'),
    path('profile/<str:pk>/', views.profile, name='profile'),
]