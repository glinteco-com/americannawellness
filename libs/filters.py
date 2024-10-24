from django.contrib.admin import SimpleListFilter
from elasticsearch_dsl.query import Wildcard


class BaseInputFilter(SimpleListFilter):
    template = "admin/input_filter.html"

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        # Grab only the "all" option.
        all_choice = next(super().choices(changelist))
        all_choice["query_parts"] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class BaseWildcardDocumentFilter(BaseInputFilter):
    document_cls = None

    def queryset(self, request, queryset):
        value = (self.value() or "").strip()

        if not value:
            return queryset

        match_obj = Wildcard(**{self.parameter_name: f"*{value}*"})
        return self.document_cls.search().query(match_obj).to_queryset()
