from rest_framework import serializers
from .models import ToDoApp, User, ToDoList, Task

class ToDoAppSerializer(serializers.ModelSerializer):
  class Meta:
    model = ToDoApp
    fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'email', 'password']


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True)
  password = serializers.CharField(write_only=True, required=True)
  password2 = serializers.CharField(write_only=True,required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2','email')
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Password fields didn't match."})
    return attrs
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user


class ToDoListSerializer(serializers.ModelSerializer):
  class Meta:
    model = ToDoList
    fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'