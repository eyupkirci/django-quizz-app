from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __init__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=50)
    date_created = models.DateField(auto_now_add=True)
    ccategory_id= models.ForeignKey(Category, on_delete=models.CASCADE)

    def __init__(self):
        return self.title

class Question(models.Model):
    title = models.TextField()
    DIFFICULTY=(
        ('1','Easy'),
        ('2', 'Normal'),
        ('3', 'Difficult'),
    )
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY)
    date_created =models.DateField(auto_now_add=True)
    date_updated =models.DateField(auto_now=True)

    def __init__(self):
        return self.title

class Answer(models.Model):
    answer_text= models.TextField()
    question_id= models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right=models.BooleanField()
    date_updated= models.DateField(auto_now=True)

    def __init__(self):
        return self.answer_text