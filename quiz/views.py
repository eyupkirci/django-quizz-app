from .models import Category, Quiz, Question, Answer
from .serializers import *

from rest_framework.generics import ListAPIView
# Create your views here.

class QuizView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryView(ListAPIView):
    serializer_class = QuizSerializer

    def get_queryset(self):
        path =self.request.path.split('/')[-1]
        cat_id = Category.objects.get(name=path).id
        queryset = Quiz.objects.filter(category_id=cat_id)

        return queryset


class TitleView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        path =self.request.path.split('/')[-1]
        cat_id = Quiz.objects.get(title=path).id
        queryset = Question.objects.filter(quiz_id=cat_id)
        #print(queryset)

        return queryset