__author__ = 'chris'

local_settings = """from os.path import join, dirname

PROJECT_ROOT = dirname(dirname(__file__))
VIRTUALENV_ROOT = dirname(PROJECT_ROOT)

DEBUG = True

MEDIA_ROOT = join(VIRTUALENV_ROOT, 'public-www', 'media')
STATIC_ROOT = join(VIRTUALENV_ROOT, 'public-www', 'static')
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = (
    '127.0.0.1',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fdb_[name]',
        'USER': 'root',
        'PASSWORD': 'blaataap',
        'HOST': '',
        'PORT': '',
    },
}

#CACHES = {
#    'default': {
#        'KEY_PREFIX': '[name]',
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': [
#            '127.0.0.1:11211',
#        ],
#    }
#}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'cd {0}/static && {1}/bin/sass --scss --compass --require bourbon.rb {{infile}} {{outfile}}'.format(PROJECT_ROOT, VIRTUALENV_ROOT)),
)

# http://projects.unbit.it/uwsgi/wiki/TipsAndTricks
# But uwsgi is only available when running under uwsgi. So ...
try:
    import uwsgi
    from uwsgidecorators import timer
    from django.utils import autoreload

    @timer(3)
    def change_code_gracefull_reload(sig):
        if autoreload.code_changed():
            uwsgi.reload()
except ImportError:
    pass
"""
