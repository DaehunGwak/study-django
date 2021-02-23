from django.db import models


class DummyTable(models.Model):
    local_field = models.IntegerField('로컬 필드', default=0, blank=True)
