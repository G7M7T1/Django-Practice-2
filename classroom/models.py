from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.subject}'
