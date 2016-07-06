import logging

from django.core.management.base import BaseCommand

from edc_content_type_map.models import ContentTypeMapHelper


logger = logging.getLogger(__name__)


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
nullhandler = logger.addHandler(NullHandler())


class Command(BaseCommand):

    args = ()
    help = 'Populate and sync content type map with django content type. (Safe)'

    def handle(self, *args, **options):
        self.stdout.write('Populating / re-populating from django content type...\n')
        ContentTypeMapHelper().populate()
        self.stdout.write('Done.')
        self.stdout.write('Syncing with membership forms, visit definitions, etc...\n')
        ContentTypeMapHelper().sync()
        self.stdout.write('Done. You may now check /admin/bhp_content_type_map/contenttypemap/.\n')
