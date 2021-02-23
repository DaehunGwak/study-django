from django.conf import settings

if settings.ENV_NAME == 'env_local':
    from testapp.model_abstracts.local import *
else:
    from testapp.model_abstracts.production import *
