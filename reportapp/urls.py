from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from reportapp.views import hello_world, AccountCreateView

app_name = 'reportapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name = 'reportapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create')#회원 가입을 할 경로를 지정해 주어야한다.
]