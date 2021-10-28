from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from users.serializers import RegisterSerializer

# Create your views here.
class RegisterAPIView(GenericAPIView):
  serializer_class=RegisterSerializer

  def post(self, request):
    serializers=self.serializer_class(data=request.data)