from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flashcard(models.Model):
    app_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="flashcards")
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=500)
    