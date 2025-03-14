from django.db import models
from django.utils.translation import gettext_lazy as _

CREATED_VERBOSE = _('Создано')
UPDATED_VERBOSE = _('Обновлено')
DELETED_VERBOSE = _('Удален')
VISIBLE_VERBOSE = _('Видимый')

namespace = 'snippets.models'


class BasicModel(models.Model):
    created_at = models.DateTimeField(CREATED_VERBOSE, auto_now_add=True)
    updated_at = models.DateTimeField(UPDATED_VERBOSE, auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    class Meta:
        abstract = True
