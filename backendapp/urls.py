from django.urls import path
from .views import RegisterDateView, UserView, RegisterDateSpecificView, UserSpecificView


urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('register/', RegisterDateView.as_view(), name='register'),
    path('register/<int:pk>', RegisterDateSpecificView.as_view(), name='register_specific'),
    path('users/<int:pk>', UserSpecificView.as_view(), name='user_specific'),
]   