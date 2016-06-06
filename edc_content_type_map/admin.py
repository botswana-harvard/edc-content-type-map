from django.contrib import admin

from .models import ContentTypeMap


@admin.register(ContentTypeMap)
class ContentTypeMapAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'id', 'model', 'app_label')
    search_fields = ('name', 'app_label', 'model')
    list_filter = ('app_label',)
