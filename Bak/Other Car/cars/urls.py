from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('review', views.rental_review, name='review'),
    path('thanks', views.thank_you, name='thanks')
]
