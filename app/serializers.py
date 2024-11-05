from rest_framework import serializers
from .models import RegisterDateModel
from django.contrib.auth.models import User


class RegisterDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterDateModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, data): #Generate a password encrypt to data
        _password = User(**data)
        _password.set_password(data["password"])
        _password.save()
        return _password
    
    def update(self, instance, data): #Generate a password encrypt from data
        _password = super().update(instance, data)
        _password.set_password(data["password"])
        _password.save()
        return _password