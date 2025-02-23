"""
    ng new
    Documentation is at: https://angular.dev/cli/new
"""

import os
from django.conf import settings
from .runner import NgRunner

def new_project(**options):
    """
    Example command:
    ng new myproject --create-application false --style scss --skip-git true --routing true\
          --directory ng --new-project-root myproject --defaults true --prefix myproject
    """
    runner = NgRunner(settings)
    project_name = options["name"]
    target_dir = options["directory"]
    if target_dir is None:
        target_dir = "."
    install_path = os.path.join(target_dir, project_name, 'ng')
    args: list = ["new", project_name, '--create-application', 'false']
    args += ['--style', 'scss', '--skip-git', 'true', '--routing', 'true']
    args += ['--directory', install_path]
    args += ['--new-project-root', project_name]
    args += ['--defaults', 'true', '--prefix', project_name]
    runner.runshell(args)
