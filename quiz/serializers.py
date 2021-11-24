from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    quiz_count = serializers.SerializerMethodField("count_of_quiz")
    def count_of_quiz(self, data):
        return len(Quiz.objects.filter(category_id=data.id))
    class Meta:
        model = Category
        fields = ["id", "name", "quiz_count"]

class QuizSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField("count_of_questions")
    def count_of_questions(self, data):
        return len(Question.objects.filter(quiz_id=data.id))

    class Meta:
        model = Quiz
        fields = ["title", "questions_count"]

class QuestionSerializer(serializers.ModelSerializer):
    answer = serializers.SerializerMethodField("count_of_questions")

    def count_of_questions(self, data):
        return Answer.objects.filter(question_id=data.id).get(is_right=True).answer_text

    class Meta:
        model = Question
        fields = ['title','difficulty', 'answer']

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = "__all__"