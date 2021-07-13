from django.urls import path

from reportapp.views import hello_world

app_name = 'reportapp'

urlpatterns = [
    path('hello_world/',hello_world, name = 'hello_world')
]