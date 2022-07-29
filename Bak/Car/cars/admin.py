from django.contrib import admin
from cars.models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car Infor', {'fields': ['brand']}),
        ('Time Infor', {'fields': ['year']})
    ]


admin.site.register(Car, CarAdmin)