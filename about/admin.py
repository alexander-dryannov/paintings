from django.contrib import admin

# from .models import About
#
# admin.site.register(About)
from solo.admin import SingletonModelAdmin
from .models import About


admin.site.register(About, SingletonModelAdmin)