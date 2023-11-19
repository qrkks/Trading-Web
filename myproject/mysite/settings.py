"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-^rh0tub&o5@d(6lf65(imoqb7f(tni2it8aikxxtxghy*_=k="
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-^rh0tub&o5@d(6lf65(imoqb7f(tni2it8aikxxtxghy*_=k=')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DEBUG', 'True')=='True'

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'grappelli',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # django-tailwind
    'tailwind',
    'theme',

    # plug in
    'django_extensions',
    'mptt',
    'django_cleanup.apps.CleanupConfig',
    'adminsortable2',
    'ckeditor',
    'ckeditor_uploader',
    'taggit',
    'widget_tweaks',
    'import_export',
    
    # apps
    'pages',
    'products',
    'search',
    'blog',
    'form_handlers',
    'utils',
    'abstractapp',
]

if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
        'django_browser_reload',
    ]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",
    # 'abstractapp.middlewares.DisableCSRFMiddleware',

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # 自定义面包屑
    # 'abstractapp.middlewares.BreadcrumbMiddleware',
]

if DEBUG:
    MIDDLEWARE += [
        # debug toolbar
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        # 自动重载
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]


ROOT_URLCONF = "mysite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / 'templates',
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # categories
                # 'abstractapp.custom_context_processors.categories',
                # 'abstractapp.custom_context_processors.inquiry_form',
                # 'abstractapp.custom_context_processors.contact',
                'abstractapp.custom_context_processors.global_context',

                # Grappelli
                # 'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = "mysite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db/db.sqlite3",
        },
        "another_db": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db copy.sqlite3",
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',  # 使用与 POSTGRES_DB 相同的值
            'USER': 'postgres',  # 使用与 POSTGRES_USER 相同的值
            'PASSWORD': 'postgres',  # 使用与 POSTGRES_PASSWORD 相同的值
            'HOST': 'postgres',  # Docker Compose 中定义的 PostgreSQL 服务名称
            'PORT': '5432',
        }
    }




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_cdn')  # 收集静态文件的目标目录

# 媒体文件设置
MEDIA_URL = 'media/'  # 媒体文件的URL前缀
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 媒体文件的存储目录

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django-tailwind Settings
TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

NPM_BIN_PATH = os.environ.get("NPM_BIN_PATH", r"C:\Program Files\nodejs\npm.cmd")

# Use IPython shell
SHELL_I = "ipython"

# Automatic file removal
CLEANUP_AUTO = True

# Age of files in days to be deleted
CLEANUP_KEEP_DAYS = 1  # Adjust this value as needed

# CKeditor
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"

# 邮件服务器
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST_USER = '34028312@qq.com'  # 你的 Gmail 地址
EMAIL_HOST_PASSWORD = 'oylpijgmzjjobiif'  # 你的 Gmail 密码


# Logging

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'log/logfile.log',
#             'formatter': 'verbose',
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }
