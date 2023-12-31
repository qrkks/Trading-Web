"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv
# 构建 server_env 文件夹中 .env 文件的完整路径
dotenv_path = Path(__file__).resolve().parent / '.env'
print('dotenv_path:', dotenv_path)
# 加载 .env 文件
load_dotenv(dotenv_path)
print('ENV_PATH from .env:', os.environ.get('ENV_PATH'))
print('DEBUG from .env:', os.environ.get('DEBUG'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG
# DEBUG = True
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
print('.env lowercase DEBUG:', os.getenv('DEBUG', 'True').lower())
print("DEBUG in settings:", DEBUG)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
"""
from django.core.management.utils import get_random_secret_key
print(f'django-insecure-{get_random_secret_key()}')

from django.contrib.sessions.models import Session
Session.objects.all().delete()
"""
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'django-insecure-sw3hbyjt)%q24^^ab^sc^=qvfr*$-1x9br5vr8&-8*9q4lo)&')


# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
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
    # 'tinymce',

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
        # auto reload
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
                'abstractapp.custom_context_processors.global_context',
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
        # "another_db": {
        #     "ENGINE": "django.db.backends.sqlite3",
        #     "NAME": BASE_DIR / "db copy.sqlite3",
        # }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
            'USER': os.environ.get('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.environ.get('POSTGRES_HOST', 'postgres'),  # 使用环境变量或默认值
            'PORT': os.environ.get('POSTGRES_PORT', '5432'),  # 使用环境变量或默认值
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

NPM_BIN_PATH = os.environ.get(
    "NPM_BIN_PATH", r"C:\Program Files\nodejs\npm.cmd")

# Use IPython shell
SHELL_I = "ipython"

# Automatic file removal
CLEANUP_AUTO = True

# Age of files in days to be deleted
CLEANUP_KEEP_DAYS = 1  # Adjust this value as needed

# CKeditor
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "ckeditor/uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'allowedContent': True,  # 是否允许编辑器插入和修改
        'autoParagraph': False,  # 是否允许自动段落
        'height': 600,  # 编辑器高度
        'width': 800,  # 编辑器宽
        'toolbar_Custom': [
            ['Source', 'Bold', 'Italic', 'Underline',
                'Blockquote', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor', 'Image', 'Smiley',
                'Link', 'Unlink', 'PasteFromWord'],
            ['JustifyCenter', 'JustifyRight', 'JustifyBlock']
        ]
    },
}

# 邮件服务器
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '465'))
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
