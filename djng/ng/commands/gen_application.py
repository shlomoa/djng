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
    ng generate application quickstart --prefix quickstart --routing true --style scss  --ssr false
    """
    runner = NgRunner(settings)
    app_name = options["name"]
    args: list = ["generate", "application", app_name]
    args += ['--style', 'scss', '--routing', 'true']
    args += ['--prefix', app_name, '--defaults', 'true']
    kwargs = {'cwd': os.path.join(os.getcwd(), 'ng')}
    runner.runshell(*args, **kwargs)
