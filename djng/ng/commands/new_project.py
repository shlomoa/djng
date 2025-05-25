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
    ng new myproject --create-application false --style scss --skip-git true --routing true \
          --directory ng --new-project-root myproject --defaults true --prefix myproject
    """
    runner = NgRunner(settings)
    project_name = options["name"]
    ng_dir = os.path.join('.', 'ng')
    install_path = os.path.abspath(ng_dir)
    if not os.path.exists(install_path):
        os.mkdir(install_path)
    args: list = ["new", project_name, '--create-application=false']
    args += ['--new-project-root=' + project_name]
    args += ['--prefix=' + project_name]
    args += ['--style=scss', '--skip-git=true', '--skip-install=true']
    args += ['--defaults=true']
    kwargs = {'cwd': install_path}
    runner.runshell(*args, **kwargs)
