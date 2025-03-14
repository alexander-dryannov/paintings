from django.urls import path

from . import views

app_name = 'about'

# urlpatterns = [
#     path('me', views.AboutListView.as_view(), name='list'),
#     path('create/', views.AboutCreateView.as_view(), name='create'),
#     # path('me/<int:pk>/', views.AboutDetailView.as_view(), name='detail'),
#     path('me/<int:pk>/update/', views.AboutUpdateView.as_view(), name='update'),
#     path('me/<int:pk>/delete/', views.AboutDeleteView.as_view(), name='delete'),
# ]

urlpatterns = [
    path('me', views.about, name='about')
]