from django.db import models

# Create your models here.
class yxTest(models.Model):
    name=models.CharField(max_length=20)
    sex=models.IntegerField(32)