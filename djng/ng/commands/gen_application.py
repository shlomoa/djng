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
    project_dirs = os.listdir(cur_dir)
    if len(project_dirs) != 1:
        raise FileExistsError("Path ng should contain one project and no more than one")
    #ng_cfg_args = ["config", "newProjectRoot"]
    #proj_name = runner.getfromshell(*ng_cfg_args, **kwargs).decode('ascii').strip()
    proj_name = project_dirs[0]
    project_path = os.path.join(install_path, proj_name)
    kwargs = {'cwd': project_path}
    args: list = ["generate", "application", app_name]
    args += ['--prefix=' + app_name]
    args += ['--project-root=' + proj_name]
    args += ['--defaults=true', '--style=scss', '--skip-install=true']
    runner.runshell(*args, **kwargs)
