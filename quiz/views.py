from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView

# Create your views here.

class QuizView(ListAPIView):
    queryset =Quiz.objects.all()
    serializer_class = QuizSerializer