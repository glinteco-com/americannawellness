from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from app.models import Information
from app.resources import InformationResource


class InformationAdmin(ImportExportModelAdmin):
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

    search_fields = [
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
        "angel_link",
        "birth_year",
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
    resource_class = InformationResource


admin.site.register(Information, InformationAdmin)
