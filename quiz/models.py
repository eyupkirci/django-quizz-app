from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    date_created = models.DateField(auto_now_add=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    title = models.CharField(max_length=255)
    DIFFICULTY=(
        ("1","Easy"),
        ("2","Normal"),
        ("3","Hard"),
    )
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Answer(models.Model):
    anwer_text = models.CharField(max_length=255)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_right= models.BooleanField()
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.anwer_text