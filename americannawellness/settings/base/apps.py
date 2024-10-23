DJANGO_APPs = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

EXTERNAL_APPS = [
    "django_extensions",
    "django_filters",
    "django_celery_beat",
    "django_celery_results",
    "import_export",
    "import_export_celery",
]
INTERNAL_APPS = ["app"]

INSTALLED_APPS = DJANGO_APPs + EXTERNAL_APPS + INTERNAL_APPS
