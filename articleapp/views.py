

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorator import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm


@method_decorator(login_required(login_url='/reports/login/'), 'get')
@method_decorator(login_required(login_url='/reports/login/'), 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    #form을 가져와 사용할 수 있게 됩니다
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    #게시글의 list 객체들의 각각의 정보를 담고 있음
    template_name = 'articleapp/list.html'
    paginate_by = 2
    #pagination을 하게 되면page_obj라는 객체가 생성된다
    #template안에서 사용가능