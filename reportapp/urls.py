from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from reportapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'reportapp'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'reportapp/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    #회원 가입을 할 경로를 지정해 주어야한다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail' ),
    # detail 같은 유형에는 특정 유저의 정보를 받아야 한다. 그 계정의 primary키를 가져오도록 한다.
    #몇 번 유저 객체에 접근 할 것인지
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]