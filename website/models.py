from django.db import models

# Create your models here.
class Feedback(models.Model):
    alias = models.CharField(max_length=40)
    feedback = models.TextField()

    
