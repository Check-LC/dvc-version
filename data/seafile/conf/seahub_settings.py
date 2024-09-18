# -*- coding: utf-8 -*-
SECRET_KEY = "b'7&n!3t&_2q2abkhona5_vh61dw$)k-bf=*f9xcaxmo6g9+b)%2'"
SERVICE_URL = "http://seafile.chaoslong.cn"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seahub_db',
        'USER': 'seafile',
        'PASSWORD': 'aad17d1a-e22c-454e-937a-fee1b0a5415f',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'memcached:11211',
    },
    'locmem': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
}
COMPRESS_CACHE_BACKEND = 'locmem'
TIME_ZONE = 'Asia/Shanghai'
FILE_SERVER_ROOT = "http://seafile.chaoslong.cn/seafhttp"
CSRF_TRUSTED_ORIGINS = ["https://seafile.chaoslong.cn"]
