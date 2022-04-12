from django.db import models
from django.utils import timezone

class Question(models.Model):
    question = models.CharField(max_length=255)
    filed = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=255)
    choice2 = models.CharField(max_length=255)
    choice3 = models.CharField(max_length=255)
    choice4 = models.CharField(max_length=255)
    answer = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    url = models.URLField()
    comprehension = models.CharField(max_length=10)
    created = models.DateTimeField(default=timezone.now())
    
    def __str__(self):
        return self.title     