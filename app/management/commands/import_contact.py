from django.core.management.base import BaseCommand, CommandError

from app.function import import_data


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument("file_paths", nargs="+", type=str)

    def handle(self, *args, **options):
        for file_path in options["file_paths"]:
            try:
                import_data(file_path=file_path)
            except Exception as err:
                raise CommandError(err)

            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully import file_path "%s"' % file_path
                )
            )
