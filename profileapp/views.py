from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        #프로파일 객체를 만드는데 보낸 form 객체가 form_valid의 form으로 들어 와있다. 실제 데이터 베이스에 저장 하지는 않고 임시 대기하도록 합니다.
        temp_profile.user = self.request.user #요청을 하는 user를 프로파일의 user로 넣는다. 즉 프로파일을 만들려고 하는 user를 프로파일의 user로 넣는 다는 것이다.
        temp_profile.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse('reportapp:detail', kwargs={'pk':self.object.user.pk})
        #여기서 self.object가 가지고 있는것은 profile 입니다.
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('reportapp:detail', kwargs={'pk':self.object.user.pk})
        #여기서 self.object가 가지고 있는것은 profile 입니다.