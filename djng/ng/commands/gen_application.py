"""
    ng generate application
    Documentation is at: https://angular.dev/cli/generate/application
"""

import os
from django.conf import settings
from .runner import NgRunner

def gen_application(**options):
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
    ng_cfg_args = ["config", "newProjectRoot"]
    kwargs = {'cwd': install_path}
    proj_name = runner.getfromshell(*ng_cfg_args, **kwargs).decode('ascii').strip()
    kwargs = {'cwd': install_path}
    args: list = ["generate", "application", app_name]
    args += ['--prefix=' + app_name]
    args += ['--project-root=' + proj_name]
    args += ['--defaults=true', '--style=scss', '--skip-install=true']
    runner.runshell(*args, **kwargs)
