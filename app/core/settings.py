from pathlib import Path

from environ import Env

env = Env()

BASE_DIR = Path(__file__).resolve().parent.parent

env.read_env(BASE_DIR.parent / ".env")

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE", default=False)

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False)

SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)

SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)

SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=False)

SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE", default=False)

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "debug_toolbar",
]

LOCAL_APPS = [
    "dashboard.apps.DashboardConfig",
    "esi.apps.EsiConfig",
    "public.apps.PublicConfig",
    "sso.apps.SsoConfig",
    "users.apps.UsersConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "templates/errors",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": env.db(),
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR.parent / ".static/"

STATICFILES_DIRS = [
    BASE_DIR / "static/",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "users.User"

ESI_CALLBACK_URL = env.str("ESI_CALLBACK_URL")

ESI_CLIENT_ID = env.str("ESI_CLIENT_ID")

ESI_SCOPES = env.str("ESI_SCOPES")

ESI_SECRET_KEY = env.str("ESI_SECRET_KEY")

SSO_AUTHORIZATION_URL = "https://login.eveonline.com/v2/oauth/authorize/"

SSO_TOKEN_URL = "https://login.eveonline.com/v2/oauth/token"

LOGIN_URL = "public:index"

LOGIN_REDIRECT_URL = "dashboard:index"

LOGOUT_URL = "sso:logout"

LOGOUT_REDIRECT_URL = "public:index"

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
    "[::1]",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "app.console": {
            "format": "[{asctime}.{msecs:0<3.0f}] {levelname} {pathname}:{funcName}:{lineno} [{process}:{thread}] {message}",  # noqa: E501
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{",
        },
    },
    "handlers": {
        "app.console": {
            "class": "logging.StreamHandler",
            "formatter": "app.console",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "app": {
            "handlers": [
                "app.console",
            ],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
