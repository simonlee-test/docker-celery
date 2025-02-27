from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Food
from .serializers import FoodSerializer
# Create your views here.

class FoodViewset(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
