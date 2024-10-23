from import_export import resources

from app.models import Contact


class ContactResource(resources.ModelResource):
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
        dataset.headers[15] = "angel_link"
        dataset.headers[16] = "birth_year"
        dataset.headers[17] = "city"
        dataset.headers[18] = "area_zip_code"
        dataset.headers[19] = "area"
        dataset.headers[20] = ""
        dataset.headers[21] = "related_code"
        dataset.headers[22] = "languages"
        dataset.headers[23] = "job"
        dataset.headers[24] = "job_categories"
        dataset.headers[25] = "job_skills"
        dataset.headers[26] = "job_tagline"

    class Meta:
        model = Contact
        batch_size = 1000
        use_bulk = True
