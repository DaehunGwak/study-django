from django.db import models


class DummyAbstractTable(models.Model):
    class Meta:
        abstract = True

    local_field = models.IntegerField('로컬 필드', default=0, blank=True)
