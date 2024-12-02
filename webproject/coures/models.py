from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class course(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True)
    course_name = models.CharField(max_length=100)
    course_teacher = models.CharField(max_length=100)