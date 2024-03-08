
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': [],
        },
    },

    'loggers': {
        logger_name: {
            'level': 'WARNING',
            'propagate': True,
        } for logger_name in (  # noqa
            'django',
            'django.request',
            'django.security',
            'django.server',
            'django.db.backends',
            'django.template',
            'musicapi',)

    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    }
}
