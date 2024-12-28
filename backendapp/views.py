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
    
class UserSpecificView(APIView):
    def get(self, request, pk):
        if pk <= 0:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(id = pk).first()
        serializer = UserSerializer(user)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if pk > 0:
            get_one_user = User.objects.filter(id = pk).first()
            data_serializer = UserSerializer(get_one_user, request.data)
            if data_serializer.is_valid():
                data_serializer.save()  
                data = {"success": "User Modified!"}
                return data
            return data_serializer.errors    
        return response.Response(status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        if pk > 0:    
            delete_user = User.objects.filter(id = pk).first()
            delete_errors = {"message": "error"}    
            if delete_user:
                delete_user.delete()            
                deleted = {"success": "User deleted!"}
                return deleted
            return delete_errors
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
    
class RegisterDateSpecificView(APIView):
    def get(self, request, pk):
        if pk <= 0:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
        register = RegisterDateModel.objects.filter(id = pk).first()
        serializer = RegisterDateSerializer(register)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        if pk > 0:
            get_one_register = RegisterDateModel.objects.filter(id = pk).first()
            data_serializer = RegisterDateSerializer(get_one_register, request.data)
            if data_serializer.is_valid():
                data_serializer.save()  
                data = {"success": "Register Modified!"}
                return data
            return data_serializer.errors    
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if pk > 0:    
            delete_register = RegisterDateModel.objects.filter(id = pk).first()
            delete_errors = {"message": "error"}    
            if delete_register:
                delete_register.delete()            
                deleted = {"success": "Register deleted!"}
                return deleted
            return delete_errors
        return response.Response(status=status.HTTP_400_BAD_REQUEST)



