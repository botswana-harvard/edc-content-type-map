from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin

from .models import ContentTypeMap


class ContentTypeMapAdmin(BaseModelAdmin):
    list_display = ('name', 'content_type', 'id', 'model', 'app_label')
    search_fields = ('name', 'app_label', 'model')
    list_filter = ('app_label',)
admin.site.register(ContentTypeMap, ContentTypeMapAdmin)
