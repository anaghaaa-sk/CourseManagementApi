from django.db import models

# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=20)
    description=models.TextField(max_length=50)
    duration=models.CharField(max_length=15)
    fee=models.IntegerField()
    level=models.CharField(max_length=20)
    image=models.ImageField(upload_to="course",null=True)