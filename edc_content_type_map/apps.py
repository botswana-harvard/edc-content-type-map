import sys

from django.apps import AppConfig
from django.db.models.signals import post_migrate


def edc_content_type_callback(sender, **kwargs):
    from edc_content_type_map.helpers import ContentTypeMapHelper
    sys.stdout.write('Running post migration for {} ...\n'.format(sender.verbose_name))
    sys.stdout.flush()
    ContentTypeMapHelper().populate()
    ContentTypeMapHelper().sync()
    sys.stdout.write(' Done. {}.\n'.format(sender.verbose_name))
    sys.stdout.flush()


class EdcContentTypeAppConfig(AppConfig):
    name = 'edc_content_type_map'
    verbose_name = 'Content Type Map'

    def ready(self):
        sys.stdout.write('Loading {} ...\n'.format(self.verbose_name))
        post_migrate.connect(edc_content_type_callback, sender=self)
