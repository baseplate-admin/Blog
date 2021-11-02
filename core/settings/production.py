from .base import *
from django.core.management import utils

SECRET_KEY = utils.get_random_secret_key()
DEBUG = False
ALLOWED_HOSTS = ["zarifahnaf.pythonanywhere.com"]
WHITENOISE_MAX_AGE = 31536000  # 1 year

try:
    from .local import *
except ImportError:
    pass
