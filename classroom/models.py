from django.db import models


# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.subject}'


class Reviews(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}'s review"
