from django.contrib import admin

# Register your models here.
from gitCoop.models import PostModel


@admin.register(PostModel)
class PostModel(admin.ModelAdmin):
    pass
