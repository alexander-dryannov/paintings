from django.contrib import admin

from . import models


# class CommentInline(admin.StackedInline):
#     model = models.Comment
#
#
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_visible']
    # inlines = [
    #     CommentInline
    # ]
