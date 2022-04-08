from django.db import models

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

    def __str__(self):
        return self.title     