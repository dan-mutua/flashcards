from rest_framework import serializers
from users.models import User

class RegisterSerializer(serializers.ModelSerializer):
  passwords = serializers.CharField(max_length=200,min_length=10,write_only=True)

  class Meta:
    model=User
    fields=('username','email', 'password')

  def create(self,validated_data):
    return User.objects.create_user(**validated_data)  