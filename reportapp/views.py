from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):

    if request.method == "POST":
        return render(request, 'reportapp/hello_world.html', context={'text':'POST METHOD!'})#template이름을 적어준다.
    else:
        return render(request, 'reportapp/hello_world.html', context={'text': 'GET METHOD!'})