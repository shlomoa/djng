""" This module expands the Django startproject command """

from django.core.management import CommandError
from django.core.management.commands.startapp import Command as BaseCommand
import djng.ng.commands as ng_commands

class Command(BaseCommand):
    """ overloading the original startproject Command"""
    ng_command = "gen_application"
    def handle(self, **options):
        self.validate(**options)
        try:
            call_back = getattr(ng_commands, self.ng_command)
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng generate application failed.") from exc

    def validate(self, **options):
        """Validate the command parameters"""
        if "name" not in options:
            raise CommandError("name must be specified.")
