"""
    ng generate application
    Documentation is at: https://angular.dev/cli/generate/application
"""

import os
from django.conf import settings
from .runner import NgRunner


def ng_build(**options):
    """
    Example command:
    ng build --output-path ../beci/app/static/angular --output-hashing none --watch
    """
    runner = NgRunner(settings)
    args: list[str] = ["build"]
    app_name = options["name"]
    if ("output_path" not in options) or (options["output_path"] is None):
        output_path = os.path.join(os.getcwd(), 'ng_dist', app_name)
    else:
        output_path = options["output_path"]
    args += ["--output-path", output_path]
    if ("output-hashing" in options) and (options["output_hashing"] is not None):
        args += ["--output-hashing", options["output_hashing"]]
    else:
        args += ["--output-hashing", "none"]
    if ("continuous" in options) and options["continuous"]:
        args += ["--watch", "true"]
    kwargs = {
        'cwd': os.path.join(os.getcwd(), 'ng'),
        'shell': True
        }
    runner.runshell(*args, **kwargs)
