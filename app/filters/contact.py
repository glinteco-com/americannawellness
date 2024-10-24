from elasticsearch_dsl.query import MultiMatch

from app.documents import ContactDocument
from libs.filters import BaseInputFilter, BaseWildcardDocumentFilter


class EmailFilter(BaseWildcardDocumentFilter):
    title = "Email"
    parameter_name = "email"
    document_cls = ContactDocument


class FirstNameFilter(BaseWildcardDocumentFilter):
    title = "First Name"
    parameter_name = "first_name"
    document_cls = ContactDocument


class LastNameFilter(BaseWildcardDocumentFilter):
    title = "Last Name"
    parameter_name = "last_name"
    document_cls = ContactDocument


class CompanyFilter(BaseWildcardDocumentFilter):
    title = "Company"
    parameter_name = "company"
    document_cls = ContactDocument


class PhoneFilter(BaseWildcardDocumentFilter):
    title = "Phone"
    parameter_name = "phone"
    document_cls = ContactDocument


class IndexedFieldsFilter(BaseInputFilter):
    title = "Search by indexing fields"
    parameter_name = "es_search"

    def queryset(self, request, queryset):
        value = (self.value() or "").strip()

        if not value:
            return queryset

        match_obj = MultiMatch(
            query=value,
            fields=[
                "email",
                "full_name",
                "first_name",
                "last_name",
                "company",
                "phone",
            ],
            fuzziness=1,
        )
        return ContactDocument.search().query(match_obj).to_queryset()
