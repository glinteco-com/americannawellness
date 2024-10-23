from import_export.formats.base_formats import CSV, XLSX

IMPORT_EXPORT_FORMATS = [XLSX, CSV]


def contact_resource():
    from app.resources import ContactResource

    return ContactResource


IMPORT_EXPORT_CELERY_INIT_MODULE = "americannawellness.celery_tasks"

IMPORT_EXPORT_CELERY_MODELS = {
    "Contact": {
        "app_label": "app",
        "model_name": "Contact",
        "resource": contact_resource,
    }
}

IMPORT_DRY_RUN_FIRST_TIME = False
