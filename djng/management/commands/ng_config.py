""" This module provides a wrapper for ng config command """
import os
from django.core.management import BaseCommand, CommandError
import djng.ng.commands as ng_commands

class Command(BaseCommand):
    """ Providing build command wrapper
    ng build --output-path ../beci/app/static/angular --output-hashing none --watch
    """
    def add_arguments(self, parser):
        parser.add_argument(
            "attribute",
            help="The attribute, could be key or key=value.")   
    def handle(self, *args, **options):
        self.validate(**options)
        try:
            call_back = getattr(ng_commands, "ng_config")
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng build failed") from exc

    def validate(self, **options):
        """ Validate correct options """
        if ("attribute" not in options) or (options["attribute"] is None):
            raise CommandError("no attribute specified")
        curr_path = os.path.join(os.getcwd(), 'ng')
        if not os.path.exists(curr_path):
            raise CommandError("ng config failed - run from root directory")
