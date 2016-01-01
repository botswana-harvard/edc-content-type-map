from django.contrib.contenttypes.models import ContentType
from django.db import models

from edc_base.model.models import BaseModel

from ..exceptions import ContentTypeMapError


class ContentTypeMapManager(models.Manager):

    def get_by_natural_key(self, app_label, model):
        content_type = ContentType.objects.get_by_natural_key(app_label, model)
        return self.get(content_type=content_type)


class ContentTypeMap(BaseModel):

    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Link to content type',
        null=True,
        blank=True)

    app_label = models.CharField(
        max_length=50,
        db_index=True)

    name = models.CharField(
        verbose_name='Model verbose_name',
        max_length=50,
        db_index=True)

    model = models.CharField(
        verbose_name='Model name (module name)',
        max_length=50,
        db_index=True)

    module_name = models.CharField(
        max_length=50,
        null=True)

    objects = ContentTypeMapManager()

    def save(self, *args, **kwargs):
        self.module_name = self.model
        super(ContentTypeMap, self).save(*args, **kwargs)

    def natural_key(self):
        return self.content_type.natural_key()

    def model_class(self):
        if self.content_type.name.lower() != self.name.lower():
            raise ContentTypeMapError(
                'ContentTypeMap.name \'{}\' is not in sync with ContentType.name \'{}\'. '
                'Run sync_content_type management command.'.format(self.name, self.content_type.name))
        if self.content_type.model != self.model:
            raise ContentTypeMapError(
                'ContentTypeMap.model \'{}\' is not in sync with ContentType.model \'{}\'. '
                'Run sync_content_type management command.'.format(self.model, self.content_type.model))
        return self.content_type.model_class()

    def __unicode__(self):
        return '{}.{}'.format(self.content_type.app_label, self.content_type.model)

    class Meta:
        app_label = 'edc_content_type_map'
        db_table = 'bhp_content_type_map_contenttypemap'
        unique_together = ['app_label', 'model', ]
        ordering = ['name', ]
