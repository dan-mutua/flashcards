from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from users.serializers import LoginSerializer, RegisterSerializer
from rest_framework import response,status
from django.contrib.auth import authenticate

# Create your views here.
class RegisterAPIView(GenericAPIView):
  serializer_class=RegisterSerializer

  def post(self, request):
    serializers=self.serializer_class(data=request.data)

    if serializers.is_valid():
      serializers.save()
      return response.Response(serializers.data,status=status.HTTP_201_CREATED)


    return response.Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)  



class LoginAPIView(GenericAPIView):

  serializer_class=LoginSerializer 


  def post(self, request):
    email = request.data.get('email', None)
    password=request.data.get('password', None)  

    user=authenticate(username=email,password=password)

    if user:
      serializer=self.serializer_class(user)

      return response.Response(serializer.data,status=status.HTTP_200_OK)
    return response.Response({'message':'invalid user!!'},status=status.HTTP_401_UNAUTHORIZED)  