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
    cur_dir = os.path.abspath('.')
    ng_dir = os.path.join('.', 'ng')
    install_path = os.path.abspath(ng_dir)
    if not os.path.exists(install_path):
        os.mkdir(install_path)
    args: list = ["new", project_name, '--create-application=false']
    args += ['--directory=' + ng_dir]
    args += ['--prefix=' + project_name]
    args += ['--style=scss', '--skip-git=true', '--skip-install=true']
    args += ['--new-project-root=.', '--defaults=true']
    kwargs = {'cwd': cur_dir}
    runner.runshell(*args, **kwargs)
