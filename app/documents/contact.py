from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from app.models import Contact


@registry.register_document
class ContactDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = "contact"
        # See Elasticsearch Indices API reference for available settings
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Contact  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            "email",
            "first_name",
            "last_name",
            "company",
            "phone",
        ]

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000
