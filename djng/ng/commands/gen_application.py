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
    cur_dir = '.'
    install_path = os.path.join(cur_dir, 'ng')
    if not os.path.exists(install_path):
        raise FileExistsError(install_path)
    kwargs = {'cwd': install_path}
    ng_cfg_args = ["config", "newProjectRoot"]
    proj_name = runner.getfromshell(*ng_cfg_args, **kwargs)
    proj_name = proj_name.decode('ascii').strip()
    args: list = ["generate", "application", app_name]
    args += ['--style', 'scss', '--routing', 'true']
    args += ['--prefix', proj_name, '--defaults', 'true']
    args += ['--project-root', os.path.join(cur_dir, app_name)]
    runner.runshell(*args, **kwargs)
