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
            default="none",
            help="Do output hashing"
        )

    def handle(self, *args, **options):
        self.validate(**options)
        try:
            call_back = getattr(ng_commands, "ng_build")
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng build failed") from exc

    def validate(self, **options):
        """ Validate correct options """
        if ("name" not in options) or (options["name"] is None):
            raise CommandError("application must have a name")
        if ("output_path" not in options) or (options["output_path"] is None):
            output_path = os.path.join(os.getcwd(), 'ng_dist')
        else:
            output_path = options["output_path"]
        curr_path = os.path.join(os.getcwd(), 'ng')
        if not os.path.exists(curr_path):
            raise CommandError("Command ng build failed - should run from project base_directory")
        if not os.path.exists(output_path):
            try:
                os.mkdir(output_path)
            except Exception as exc:
                raise CommandError("Command ng build failed to to create:" + output_path) from exc
