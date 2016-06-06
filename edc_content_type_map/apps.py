import sys

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def edc_content_type_callback(sender, **kwargs):
    from edc_content_type_map.helpers import ContentTypeMapHelper
    sys.stdout.write('Loading {} ...\n'.format(sender.verbose_name))
    ContentTypeMapHelper().populate()
    ContentTypeMapHelper().sync()


class EdcContentTypeAppConfig(AppConfig):
    name = 'edc_content_type_map'
    verbose_name = 'Content Type Map'

    def ready(self):
        post_migrate.connect(edc_content_type_callback, sender=self)
