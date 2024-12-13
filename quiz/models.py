from django.db import models
from djongo.models.fields import ObjectIdField  # Import ObjectIdField for MongoDB compatibility

class QuizUser(models.Model):
    id = ObjectIdField(primary_key=True)  # Define ObjectIdField as the primary key
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Question(models.Model):
    text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=1)  # Store correct option as "A", "B", "C", or "D"

    def __str__(self):
        return self.text

class QuizResult(models.Model):
    user = models.ForeignKey(QuizUser, on_delete=models.CASCADE)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}/5"
