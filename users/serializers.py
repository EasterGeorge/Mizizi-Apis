from rest_framework import serializers

from users.models import CustomUser, FirstAidProcedure, MiziziUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'phoneNumber', 'paymentMethod']


class FirstAidSerializer(serializers.ModelSerializer):

    class Meta:
        model = FirstAidProcedure
        fields = ['id', 'title', 'category', 'text','image']

class MiziziUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MiziziUser 
        fields = ('id', 'name', 'email', 'phoneNumber', 'password','paymentMethod', 'registrationDate')