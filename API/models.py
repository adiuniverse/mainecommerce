from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length = 20 )
    student_age = models.IntegerField()
    student_address = models.CharField(max_length = 100)
    student_phone = models.BigIntegerField()
    student_email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)

    class Meta:
        db_table = 'student'