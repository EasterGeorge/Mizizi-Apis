#from django.shortcuts import 

from .models import FirstAidProcedure, MiziziUser
from .serializers import FirstAidSerializer, MiziziUserSerializer
from rest_framework import generics

class FirstAidListCreate(generics.ListCreateAPIView):
    queryset = FirstAidProcedure.objects.all()
    serializer_class = FirstAidSerializer

class FirstAidList(generics.ListAPIView):
    queryset = FirstAidProcedure.objects.all()
    serializer_class = FirstAidSerializer
   
class MiziziUserListCreate(generics.ListCreateAPIView):
    queryset = MiziziUser.objects.all()
    serializer_class = MiziziUserSerializer

class MiziziUserList(generics.ListAPIView):
    queryset = MiziziUser.objects.all()
    serializer_class = MiziziUserSerializer
   
