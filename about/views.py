from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import About


# class AboutListView(generic.ListView):
#     model = About
#     queryset = About.objects.filter(is_visible=True).order_by('-pk')
#     context_object_name = 'about'
#     template_name = 'about/list.html'


# class AboutCreateView(LoginRequiredMixin, generic.CreateView):
#     model = About
#     template_name = 'about/create.html'
#     fields = ['title', 'text', 'photo', 'is_visible']
#     success_url = reverse_lazy('about:list')
#     raise_exception = True


# class AboutDetailView(generic.DetailView):
#     model = About
#     template_name = 'about/detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['obj'] = self.get_object()
#         context['detail'] = True
#         return context


# class AboutUpdateView(LoginRequiredMixin, generic.UpdateView):
#     model = About
#     template_name = 'about/update.html'
#     fields = ['title', 'text', 'photo', 'is_visible']
#     raise_exception = True


# class AboutDeleteView(LoginRequiredMixin, generic.DeleteView):
#     model = About
#     template_name = 'about/delete.html'
#     success_url = reverse_lazy('about:list')
#     raise_exception = True

from django.shortcuts import render

def about(request):
    solo = About.objects.first()
    return render(request, 'about/solo.html', {})
