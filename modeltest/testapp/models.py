from django.conf import settings
from django.db import models


print(settings.ENV_NAME)


class DummyTable(models.Model):
    if settings.ENV_NAME == 'env_local':
        local_field = models.IntegerField('로컬 필드', default=0, blank=True)
    else:
        production_field = models.IntegerField("프로덕션 필드", default=1, blank=False)
