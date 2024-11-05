from django.urls import path
from .views import RegisterDateView, UserView


urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('register/', RegisterDateView.as_view(), name='register'),
]   