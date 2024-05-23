from .models import Students
from rest_framework import serializers
from django.contrib.auth.models import User

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
       model=Students
       fields='__all__'
       
       
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user