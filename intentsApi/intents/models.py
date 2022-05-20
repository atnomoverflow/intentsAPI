from django.db import models

# Create your models here.
class Intents(models.Model):
    tag = models.CharField(max_length=30)
    patterns=models.JSONField()
    responses=models.JSONField()
