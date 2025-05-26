"""
    ng generate application
    Documentation is at: https://angular.dev/cli/generate/application
"""

import os
from django.conf import settings
from .runner import NgRunner

def ng_gen_app(**options):
    """
    Example command:
    ng generate application tutorial --prefix myproject \
        --routing true --style scss  --ssr false \
        --project-root . --default true
    """
    runner = NgRunner(settings)
    app_name = options["name"]
    cur_dir = os.path.join('.', 'ng')
    install_path = os.path.abspath(cur_dir)
    if not os.path.exists(install_path):
        raise FileExistsError(install_path)
    kwargs = {'cwd': install_path}
    args: list = ["generate", "application", app_name]
    args += ['--prefix=' + app_name] # determines selector name
    args += ['--defaults=true', '--style=scss', '--skip-install=true']
    runner.runshell(*args, **kwargs)
