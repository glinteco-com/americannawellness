from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.filters.contact import (
    CompanyFilter,
    EmailFilter,
    FirstNameFilter,
    IndexedFieldsFilter,
    LastNameFilter,
    PhoneFilter,
)
from app.models import Contact
from app.resources import ContactResource


class ContactAdmin(ImportExportModelAdmin):
    list_display = [
        "email",
        "full_name",
        "first_name",
        "last_name",
        "position",
        "country",
        "city_zip_code",
        "user_linkedin",
        "company",
        "phone",
        "facebook",
        "company_linkedin",
        "twitter",
        "website",
        "birth_year",
        "angel_link",
        "city",
        "area_zip_code",
        "area",
        "related_code",
        "languages",
        "job",
        "job_categories",
        "job_skills",
        "job_tagline",
    ]

    list_filter = [
        IndexedFieldsFilter,
        EmailFilter,
        FirstNameFilter,
        LastNameFilter,
        CompanyFilter,
        PhoneFilter,
    ]

    resource_class = ContactResource


admin.site.register(Contact, ContactAdmin)
