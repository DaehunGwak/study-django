from django.db import models


class DummyAbstractTable(models.Model):
    class Meta:
        abstract = True

    production_field = models.IntegerField('프로덕션 필드', default=1, blank=True)
