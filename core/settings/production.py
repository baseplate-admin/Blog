from .base import *


DEBUG = False
# ALLOWED_HOSTS = ["127.0.0.1"]
WHITENOISE_MAX_AGE = 31536000  # 1 year

try:
    from .local import *
except ImportError:
    pass
