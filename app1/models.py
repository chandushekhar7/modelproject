from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length = 40)
    addr = models.CharField(max_length = 40)

    class Meta:
        db_table = "Student"
        managed = True

    def __str__(self):
        return self.name
