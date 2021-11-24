from django.contrib import admin
from .models import Category, Quiz, Question, Answer
import nested_admin

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline]

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz,QuizAdmin)