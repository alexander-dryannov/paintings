from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from snippets.models.models import BasicModel


# class About(BasicModel):
#     title = models.CharField(_('Заглавие'), max_length=255)
#     text = models.TextField(_('Обо мне'))
#     photo = models.ImageField(_('Моя фотография'), upload_to='my_photo/%Y/%m/%d')
#
#     def get_absolute_url(self):
#         return reverse('about:detail', args=[self.pk, ])
#
#     def get_update_url(self):
#         return reverse('about:update', args=[self.pk, ])
#
#     def get_delete_url(self):
#         return reverse('about:delete', args=[self.pk, ])
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Обо мне'
#         verbose_name_plural = 'Обо мне'


from solo.models import SingletonModel


class About(SingletonModel, BasicModel):
    first_name = models.CharField('Имя', max_length=255, default='Имя')
    last_name = models.CharField('Фамилия', max_length=255, default='Фамилия')
    middle_name = models.CharField('Отчество', max_length=255, default='Отчество', blank=True)
    about_us = models.TextField('Обо мне')
    image = models.ImageField('Фотография', upload_to='my_photo/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Обо мне'

    class Meta:
        verbose_name = 'Обо мне'
