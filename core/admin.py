from django.contrib import admin

from core.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'is_published')
    list_filter = ('created', 'is_published')
    search_fields = ('title',)
