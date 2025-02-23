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
    if "output_path" not in options:
        output_path = os.path.join(os.getcwd(), options["name"])
    else:
        output_path = options["output_path"]
    args += ["--output_path", output_path]
    if "output-hashing" in options:
        args += ["--output-hashing", options["output_hashing"]]
    else:
        args += ["--output-hashing", "none"]
    if "continuous" in options:
        args += ["--watch"]
    kwargs = {'cwd': os.path.join(os.getcwd(), 'ng')}
    runner.runshell(*args, **kwargs)
