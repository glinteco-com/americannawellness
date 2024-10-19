from import_export import resources

from app.models import Information


class InformationResource(resources.ModelResource):
    def before_import(self, dataset, **kwargs):
        dataset.headers[0] = "email"
        dataset.headers[1] = ""
        dataset.headers[2] = "first_name"
        dataset.headers[3] = "last_name"
        dataset.headers[4] = "position"
        dataset.headers[5] = "country"
        dataset.headers[6] = "city_zip_code"
        dataset.headers[7] = "user_linkedin"
        dataset.headers[8] = "company"
        dataset.headers[9] = ""
        dataset.headers[10] = "phone"
        dataset.headers[11] = "facebook"
        dataset.headers[12] = "company_linkedin"
        dataset.headers[13] = "twitter"
        dataset.headers[14] = "website"
        dataset.headers[15] = "birth_year"
        dataset.headers[16] = "city"
        dataset.headers[17] = "area_zip_code"
        dataset.headers[18] = "area"
        dataset.headers[19] = ""
        dataset.headers[20] = "related_code"
        dataset.headers[21] = "languages"
        dataset.headers[22] = "job"
        dataset.headers[23] = "job_categories"
        dataset.headers[24] = "job_skills"
        dataset.headers[25] = "job_tagline"

    class Meta:
        model = Information
