from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9(j58y(0#nxf=*y4!k=plybto4dc7j$qiqo0gm9_w_!0y0381p"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WHITENOISE_MAX_AGE = 0

try:
    from .local import *
except ImportError:
    pass
