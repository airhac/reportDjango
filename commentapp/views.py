from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorator import Comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment



class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'
    #Form형태를 보여줄 html
    def form_valid(self, form):
        #temp_comment = form.save(commit=False)
        #temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        #숫자로 넣으려면 DB에 접근 해야한다.
        #다른 방법도 있음 instance는 객체
        #self.request.POST.get('article_pk')
        #temp_comment.writer = self.request.user
        #temp_comment.save()
        #이러한 식으로 작성하는 이유는 form으로 content만 들어오고 관련 데이터는 null로 저장 되게 됩니다. 그래서
        #form의 형태를 바꿔주는 것 입니다.
        #create.html에서 hidden으로 보낸 article_pk가 이 쪽으로 넘어 옵니다.
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')#
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
        #object는 현재 댓글(객체)이고 그 댓글의 게시글의 pk를 찾아 보내준다.

@method_decorator(Comment_ownership_required, 'get')
@method_decorator(Comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
        # object는 현재 댓글(객체)이고 그 댓글의 게시글의 pk를 찾아 보내준다.
