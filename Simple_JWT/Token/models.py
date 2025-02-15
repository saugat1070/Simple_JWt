from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    class_room = models.CharField(max_length=5)
    id_number = models.IntegerField()

    def __str__(self):
        return self.name