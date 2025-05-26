""" This module provides a wrapper for ng-openapi-gen command """

import os
import re
from django.core.management import BaseCommand, CommandError
import djng.ng.commands as ng_commands

class Command(BaseCommand):
    """ Providing build command wrapper
    npx ng-openapi-gen --input ../schema.yml --output quetionaire/src/app/openapi
    """
    def add_arguments(self, parser):
        parser.add_argument("--input",                            
                            action="store",
                            dest="input",
                            required=True,
                            help="Path for OAS yml file.")
        parser.add_argument("--output",
                            action="store",
                            dest="output",
                            required=True,
                            help="Output path for ng-openapi-new")

    def handle(self, *args, **options):
        self.validate(**options)
        try:
            call_back = getattr(ng_commands, "ng_openapi_gen")
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng_openapi_gen failed") from exc

    def validate(self, **options):
        """ Validate correct options """
        if ("input" not in options) or (options["input"] is None):
            raise CommandError("must provide input")
        else:
            input = options["input"]
        if ("output" not in options) or (options["output"] is None):
            raise CommandError("must provide output")
        if not os.path.exists(input):
            raise FileNotFoundError("Input file " + input + " doesn't exist")
