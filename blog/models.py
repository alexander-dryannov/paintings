from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from snippets.models.models import BasicModel

USER = get_user_model()


class Post(BasicModel):
    title = models.CharField(_('Название публикации'), max_length=255)
    text = models.TextField(_('Текст публикации'))

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk, ])

    def get_update_url(self):
        return reverse('blog:post_update', args=[self.pk, ])

    def get_delete_url(self):
        return reverse('blog:post_delete', args=[self.pk, ])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


# class Comment(BasicModel):
#     first_name = models.CharField(_('Имя'), max_length=255)
#     last_name = models.CharField(_('Фамилия'), max_length=255)
#     email = models.EmailField(_('Адрес электронной почты'))
#     commented_post = models.ForeignKey(Post, verbose_name=_('Комментируемый пост'), on_delete=models.PROTECT, related_name='comments')
#     comment_text = models.TextField(_('Комментарий'))
#
#     def __str__(self):
#         return self.first_name + self.last_name
#
#     class Meta:
#         verbose_name = 'Комментарий'
#         verbose_name_plural = 'Комментарии'
