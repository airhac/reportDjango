from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'reportapp/hello_world.html')#template이름을 적어준다.

