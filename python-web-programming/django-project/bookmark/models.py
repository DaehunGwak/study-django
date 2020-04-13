"""
모델을 만들 땐 models.py 에 작성하고
admin.py 에 등록해주어야 함
"""
from django.db import models


class Bookmark(models.Model):
    url = models.URLField('URL', unique=True)
    title = models.CharField('TITLE', max_length=100, blank=True)

    def __str__(self):
        return self.title
