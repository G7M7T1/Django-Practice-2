from django.shortcuts import render, redirect
from django.urls import reverse
from . import models


# Create your views here.
def lst(req):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(req, 'cars/list.html', context)


def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')


def delete(req):
    if req.POST:
        car_id = req.POST['pk']
        try:
            models.Car.objects.get(pk=car_id).delete()
            return redirect(reverse('cars:list'))
        except:
            return redirect(reverse('cars:list'))

    return render(req, 'cars/delete.html')
