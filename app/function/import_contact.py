import tablib

from app.resources import ContactResource


def import_data(file_path):
    dataset = tablib.Dataset()
    with open(file_path, "rb") as fh:
        dataset.load(fh, format="xlsx")

    resource = ContactResource()
    result = resource.import_data(dataset=dataset, dry_run=False)
    if result.has_errors():
        print("Error")
    print("Success")
