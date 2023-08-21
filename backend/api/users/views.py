from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def user_list(request):
    match request.method:
        
        case "GET":
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return JsonResponse({"users" : serializer.data}, safe=False)
        
        case "POST":
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])    
def user_detail(request, private_key):
    
    try:
        user = User.objects.get(private_key=private_key)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    match request.method:
        case "GET":
            serializer = UserSerializer(user)
            return Response(serializer.data)
        
        case "PUT":
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        case "DELETE":
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

