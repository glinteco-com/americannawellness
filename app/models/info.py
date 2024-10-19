from django.db import models


class Information(models.Model):
    email = models.EmailField(
        max_length=1024, default="", blank=True, null=True
    )
    full_name = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    first_name = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    last_name = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    position = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    country = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    city_zip_code = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )

    user_linkedin = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    company = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    phone = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    facebook = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    company_linkedin = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )

    twitter = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    website = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    angel_link = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )

    birth_year = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    city = models.CharField(max_length=1024, default="", blank=True, null=True)
    area_zip_code = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )
    area = models.CharField(max_length=1024, default="", blank=True, null=True)
    related_code = models.CharField(
        max_length=1024, default="", blank=True, null=True
    )

    languages = models.CharField(
        max_length=2028, default="", blank=True, null=True
    )
    job = models.CharField(max_length=2028, default="", blank=True, null=True)
    job_categories = models.TextField(
        max_length=2048, default="", blank=True, null=True
    )
    job_skills = models.TextField(
        max_length=2048, default="", blank=True, null=True
    )
    job_tagline = models.TextField(
        max_length=2028, default="", blank=True, null=True
    )
