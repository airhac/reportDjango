from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from reportapp.decorators import account_ownership_required
from reportapp.models import HelloWorld

has_ownership = [
    account_ownership_required, login_required(login_url='/reports/login/')
]

# 장고 자체에서 제공해주는 decorator
def hello_world(request):

        if request.method == "POST":
            temp = request.POST.get('hello_world_input')
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            #hello_world_list = HelloWorld.objects.all()
            #request에서 post method 중에서 get은 hello_world_input이라는 이름을 가진 데이터를 가지고 와라
            #return render(request, 'reportapp/hello_world.html', context={'hello_world_list': hello_world_list})#template이름을 적어준다.
            return HttpResponseRedirect(reverse('reportapp:hello_world'))
            #여기서 reverse함수는 urls.py에서 설정한 URL의 name이나, viewname을 통해서 다시 url로 되돌릴 수 있다.
        else:
            hello_world_list = HelloWorld.objects.all()
            # request에서 post method 중에서 get은 hello_world_input이라는 이름을 가진 데이터를 가지고 와라
            return render(request, 'reportapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):#CreateView를 상속받는다.
    model = User #장고에서 기본적으로 제공해주는 모델
    #User Model을 만드는데 필요한 form 이 필요
    form_class = UserCreationForm
    success_url = reverse_lazy('reportapp:hello_world')#어느 계정으로 다시 재 연결 할 것인가
    template_name = 'reportapp/create.html'#회원가입을 할때 어는 html을 이용하여 from을 볼지 설정 해주어야한다.

class AccountDetailView(DetailView,MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    #이부분은 우리가 확인하고 싶은 유저의 정보를 볼수 있도록 확인하고자 하는 pk의 유저를 가지고 있어야한다.
    #template에서 사용하는 user객체 이름을 다르게 설정 할 수 가 있다.
    template_name = 'reportapp/detail.html'

    paginate_by = 4
    def get_context_data(self, **kwargs):
        object_list=Article.objects.filter(writer=self.get_object())
        #현재 project와 같은 article을 filtering해서 object_list에 넣어 줍니다.
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)
        #template 창에서 dl object_list를 사용 할 수 있게 됩니다.

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
#일반 function에 사용하는 decorator를 method에 사용할 수 있도록 변환해주는 decorator이다.
class AccountUpdateView(UpdateView):#CreateView를 상속받는다.
    model = User
    #장고에서 기본적으로 제공해주는 모델
    #User Model을 만드는데 필요한 form 이 필요
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('reportapp:hello_world')
    #어느 계정으로 다시 재 연결 할 것인가
    template_name = 'reportapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('reportapp:login')
    template_name = 'reportapp/delete.html'

