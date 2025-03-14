from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('paintings/', views.GalleryListView.as_view(), name='list'),
    path('painting/create/', views.GalleryCreateView.as_view(), name='create'),
    # path('painting/<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('painting/<int:pk>/update/', views.GalleryUpdateView.as_view(), name='update'),
    path('painting/<int:pk>/delete/', views.GalleryDeleteView.as_view(), name='delete'),
]
