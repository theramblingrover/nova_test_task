import logging

from .debug import DEBUG

LOG_FORMAT_STRING = "%(asctime)s %(levelname)s [%(name)s in %(funcName)s %(pathname)s:%(lineno)d]\n%(message)s" if DEBUG else "%(asctime)s %(levelname)s %(message)s"


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    "formatters": {"standard": {"format": LOG_FORMAT_STRING}},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },

    'loggers': {
        "": {
            "handlers": ["console"],
            "level": logging.DEBUG if DEBUG else logging.INFO,
            "propagate": True,
        },
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True,
        },
        'uvicorn': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
