from django.db import models
from bson import ObjectId

def generate_object_id():
    return str(ObjectId())

class QuizUser(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_object_id)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


    class Meta:
        db_table = "quiz_quizuser"  # Explicitly set the table name


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
