from app.models import Information
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from app.resources import InformationResource
import openpyxl


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