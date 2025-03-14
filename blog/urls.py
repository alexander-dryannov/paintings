from django.urls import path

from . import views as v

app_name = 'blog'

urlpatterns_post = [
    path('', v.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', v.PostDetail.as_view(), name='post_detail'),
    path('post/create', v.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update', v.PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete', v.PostDelete.as_view(), name='post_delete'),
]

urlpatterns_comment = [
    # path('', v.CommentList.as_view(), name='comment_list'),
    # path('<int:pk>', v.CommentDetail.as_view(), name='comment_detail'),
    # path('<int:pk>/create', v.CommentCreate.as_view(), name='comment_create'),
    # path('<int:pk>/update', v.CommentUpdate.as_view(), name='comment_update'),
    # path('<int:pk>/delete', v.CommentDelete.as_view(), name='comment_delete'),
]

urlpatterns = urlpatterns_post + urlpatterns_comment
