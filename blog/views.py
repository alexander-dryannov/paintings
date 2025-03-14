from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from blog import models


class PostList(generic.ListView):
    model = models.Post
    queryset = models.Post.objects.filter(is_visible=True).order_by('-pk')
    context_object_name = 'posts'
    template_name = 'post/list.html'
    paginate_by = 7


class PostDetail(generic.DetailView):
    model = models.Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['obj'] = self.get_object()
        context['detail'] = True
        return context


class PostUpdate(LoginRequiredMixin, generic.UpdateView):
    model = models.Post
    template_name = 'post/update.html'
    fields = ['title', 'text', 'is_visible']
    raise_exception = True


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    template_name = 'post/create.html'
    fields = ['title', 'text', 'is_visible']
    success_url = reverse_lazy('blog:post_list')
    raise_exception = True


class PostDelete(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('blog:post_list')
    raise_exception = True


# class CommentList(generic.ListView):
#     model = models.Comment
#     queryset = Comment.objects.filter(is_visible=True).order_by('-pk')
#     context_object_name = 'posts'
#     template_name = 'comment/list.html'
#     paginate_by = 7
# 
# 
# class CommentDetail(generic.DetailView):
#     model = models.Comment
#     template_name = 'comment/detail.html'
# 
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['obj'] = self.get_object()
#         context['detail'] = True
#         return context
# 
# 
# class CommentUpdate(generic.UpdateView):
#     model = models.Comment
#     template_name = 'comment/update.html'
#     fields = ['post_title', 'post_text', 'is_visible']
#     raise_exception = True
# 
# 
# class CommentCreate(generic.CreateView):
#     model = models.Comment
#     template_name = 'comment/create.html'
#     fields = ['post_title', 'post_text', 'is_visible']
#     success_url = reverse_lazy('blog:comment_list')
#     raise_exception = True
# 
# 
# class CommentDelete(generic.DeleteView):
#     model = models.Comment
#     template_name = 'comment/delete.html'
#     success_url = reverse_lazy('blog:comment_list')
#     raise_exception = True
