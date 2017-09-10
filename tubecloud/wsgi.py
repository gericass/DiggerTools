"""
WSGI config for tubecloud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

'''
from dj_static import Cling
import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tubecloud.settings")

application = Cling(get_wsgi_application())
#application = DjangoWhiteNoise(application)


'''
import os
import keijiban.bach_script as logger
import time
from multiprocessing import Pool
import multiprocessing as multi


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tubecloud.settings")


from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise



application = get_wsgi_application()
application = DjangoWhiteNoise(application)


p = Pool(multi.cpu_count())
p.map(logger.access(),list(range(2)))

