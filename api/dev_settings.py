# -*- coding: utf-8 -*-
PROJECT = 'Django REST Skeleton (Dev)'
HOST = 'http://localhost'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database-name',
        'USER': 'database-user',
        'PASSWORD': 'database-password',
        'HOST': '',
        'PORT': '',
    },
}
