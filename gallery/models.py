from django.db import models
from django.urls import reverse

from snippets.models.models import BasicModel


class Gallery(BasicModel):
    image = models.ImageField('Картина', upload_to='paintings/%Y/%m/%d')
    width = models.PositiveIntegerField('Ширина', default=0)
    height = models.PositiveIntegerField('Ширина', default=0)

    def get_absolute_url(self):
        return reverse('gallery:detail', args=[self.slug, ])

    def get_update_url(self):
        return reverse('gallery:update', args=[self.slug, ])

    def get_delete_url(self):
        return reverse('gallery:delete', args=[self.slug, ])

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    def __str__(self):
        return self.image.name
