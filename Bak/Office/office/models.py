from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(110)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):
        return f"{self.last_name} {self.first_name} is {self.age} years old"

# python manage.py shell
# from office.models import Patient
# Patient.objects.all()

# <QuerySet [<Patient: Smith Carl is 26 years old>, <Patient: Cyan Susan is 40 years old>,
# <Patient: Leo Yuri is 56 years old>]>
