from settings import *

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['dev']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['qa']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['prod']['ENGINE'] = 'django.db.backends.sqlite3'