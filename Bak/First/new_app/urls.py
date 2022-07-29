from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    path('', views.new_index, name='index'),
    path('variable', views.variable_view, name='variable'),
    path('new-page', views.new_page, name='new-page')
]