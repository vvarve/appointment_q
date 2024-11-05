from .serializers import RegisterDateSerializer, UserSerializer, User
from rest_framework import response, status
from rest_framework.views import APIView
from .models import RegisterDateModel

class RegisterDateView(APIView):
    def post(self, request):
        serializer = RegisterDateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        registers = RegisterDateModel.objects.all()
        serializer = RegisterDateSerializer(registers, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)



