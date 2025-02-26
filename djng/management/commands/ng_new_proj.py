""" This module expands the Django startproject command """
import os
from django.core.management import CommandError
from django.core.management.commands.startproject import Command as BaseCommand
import djng.ng.commands as ng_commands

class Command(BaseCommand):
    """ overloading the original startproject Command"""
    ng_command = "new_project"
    def handle(self, **options):
        self.validate(**options)
        try:
            call_back = getattr(ng_commands, self.ng_command)
            call_back(**options)
        except AttributeError as exc:
            raise CommandError("Command ng new failed.") from exc

    def validate(self, **options):
        """Validate the command parameters"""
        if "name" not in options:
            raise CommandError("name must be specified.")
        project_name = options["name"]
        target_dir = '.'
        if hasattr(options, "directory") and options["directory"] is not None:
            target_dir = options["directory"]
        install_path = os.path.join(target_dir, project_name, 'ng')
        if os.path.exists(install_path):
            raise CommandError(f"{install_path} already exists.")
