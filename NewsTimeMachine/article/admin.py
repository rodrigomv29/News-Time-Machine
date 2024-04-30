from django.contrib import admin

# Register your models here.

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author_name", "pub_date")
