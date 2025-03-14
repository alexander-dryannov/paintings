from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.views.generic.edit import FormView
from PIL import Image

from .forms import GalleryForm
from .models import Gallery

# TODO: Поворот изображения
# @csrf_exempt
# def rotate_image(request, slug):
#     angle = json.loads(request.body)
#     image = GalleryImage.objects.get(slug=slug)
#     p = Path(__file__).resolve().parent.parent.joinpath(
#         settings.MEDIA_ROOT).joinpath(str(image.src))
#     print(p)
#     im = Image.open(p)
#     e = im.getexif()
#     print(e)
#     im = im.rotate(angle.get('angle'), expand=True)
#     im.save(p)
#     return HttpResponse(
#         json.dumps({'status': 200}),
#         content_type="application/json"
#         )


class GalleryListView(ListView):
    model = Gallery
    queryset = Gallery.objects.filter(is_visible=True)
    context_object_name = 'paintings'
    template_name = 'list.html'


# class GalleryDetailView(DetailView):
#     model = Gallery
#     template_name = 'detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['obj'] = self.get_object()
#         context['detail'] = True
#         return context


class GalleryCreateView(LoginRequiredMixin, FormView):
    form_class = GalleryForm
    template_name = 'create.html'
    success_url = reverse_lazy('gallery:list')
    raise_exception = True

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        paintings = form.cleaned_data['paintings']
        for painting in paintings:
            image = Image.open(painting)
            width, height = image.size
            Gallery.objects.create(image=painting, width=width, height=height)
        return super().form_valid(form)


class GalleryUpdateView(LoginRequiredMixin, UpdateView):
    model = Gallery
    template_name = 'update.html'
    fields = '__all__'
    raise_exception = True


class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = Gallery
    template_name = 'delete.html'
    success_url = reverse_lazy('gallery:list')
    raise_exception = True
