#Converts from python data to json
from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = ['id', 'fname', 'lname', 'email']
        fields = '__all__';