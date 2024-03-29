from .base import *


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.production.sqlite3',
    }
}


# 환경 이름

ENV_NAME = 'env_production'
