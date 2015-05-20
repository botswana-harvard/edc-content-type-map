import factory

from django.contrib.contenttypes.models import ContentType

from edc_base.model.tests.factories import BaseModelFactory


class ContentTypeFactory(BaseModelFactory):
    class Meta:
        model = ContentType

    name = factory.Sequence(lambda n: 'contenttypemap{0}'.format(n))
    app_label = 'edc_content_type_map'
    model = factory.Sequence(lambda n: 'contenttypemap{0}'.format(n))
