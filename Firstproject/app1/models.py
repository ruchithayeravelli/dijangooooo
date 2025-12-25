from django.db import models

# Create your models here.
class students(models.Model):
    stud_name=models.CharField(max_length=100)
    stud_age=models.IntegerField()
    stud_gender=models.CharField(max_length=100)
    stud_email=models.EmailField(unique=True)
