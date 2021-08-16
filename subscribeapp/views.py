from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required(login_url='/reports/login/'), 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        user = self.request.user
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))

        subsciption = Subscription.objects.filter(user=user,
                                                  project=project)
        if subsciption.exists():
            subsciption.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)

@method_decorator(login_required(login_url='/reports/login/'), 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 3
    #이 안에서 가지고 오는 게시글들에 조건을 부여 할 수 있는 함수
    def get_queryset(self):
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        #user 와 구독을 하고 있는 프로젝트들을 찾아 와야합니다. value_list는 가지고온 값들을 리스트 시킨다는 의미
        #이 projects에는 user가 구독한 모든 project들이 담기게 됩니다.
        article_list = Article.objects.filter(project__in=projects)
        return article_list