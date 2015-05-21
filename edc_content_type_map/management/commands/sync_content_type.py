import logging

from django.core.management.base import BaseCommand

from ...classes import ContentTypeMapHelper


logger = logging.getLogger(__name__)


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
nullhandler = logger.addHandler(NullHandler())


class Command(BaseCommand):

    args = ()
    help = 'Populate and sync content type map with django content type. (Safe)'

    def handle(self, *args, **options):
        print('Populating / re-populating from django content type...')
        ContentTypeMapHelper().populate()
        print('Done.')
        print('Syncing with membership forms, visit definitions, etc...')
        ContentTypeMapHelper().sync()
        print('Done. You may now check /admin/edc_content_type_map/contenttypemap/.')