from .base import config_parser

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": config_parser.get(
            "ES", "HOST", fallback="http://localhost:9200"
        ),
        # NOTE: temporary not use auth for developing
        # "http_auth": ("username", "password"),
    }
}

ELASTICSEARCH_DSL_AUTOSYNC = False  # Due to business, we must import a lot of data at a time, we must do bulk insert, and then manually populate ES after finishing importing data.
