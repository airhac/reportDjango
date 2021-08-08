from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name ='articleapp'

urlpatterns =[
    path('list/', ArticleListView.as_view(), name='list'),
    #Template만 지정해주면 알아서 다 만들어 줍니다.
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]