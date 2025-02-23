""" This module provides a wrapper for ng build command """
import os
from django.core.management import BaseCommand, CommandError
import djng.ng.commands as ng_commands

class Command(BaseCommand):
    """ Providing build command wrapper
    ng build --output-path ../beci/app/static/angular --output-hashing none --watch
    """
    def add_arguments(self, parser):
        parser.add_argument("name",
                            help="Name of the application or project.")
        parser.add_argument("--output-path",
                            action="store",
                            dest="output_path",
                            help="The output path of ng build")
        parser.add_argument(
            "--cont",
            action="store_true",
            dest="continuous",
            help="Continuous build option",
        )
        parser.add_argument(
            "--output-hashing",
            action="store",
            dest="output_hashing",
            help="Do output hashing"
        )

    def handle(self, *args, **options):
        if "name" not in options:
            raise CommandError("application must have a name")
        if "output_path" not in options:
            output_path = os.path.join(os.getcwd(), 'ng', options["name"])
        else:
            output_path = options["output_path"]
        if not os.path.exists(output_path):
            raise CommandError("Command ng build failed, output path does not exist")
        try:
            call_back = getattr(ng_commands, "ng_build")
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng build failed") from exc
