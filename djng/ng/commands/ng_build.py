"""
    ng generate application
    Documentation is at: https://angular.dev/cli/generate/application
"""

import os
from django.conf import settings
from .runner import NgRunner, NpmRunner


def ng_build(**options):
    """
    Example command:
    ng build --output-path ../beci/app/static/angular --output-hashing none --watch
    """
    args: list[str] = ["build"]
    app_name = options["name"]
    args += [app_name]
    if "output_path" in options and options['output_path'] is not None:
        args += ["--output-path=" + options["output_path"]]
    if "output-hashing" in options and options["output_hashing"] is not None:
        args += ["--output-hashing=" + options["output_hashing"]]
    else:
        args += ["--output-hashing=none"]
    if ("continuous" in options) and options["continuous"]:
        args += ["--watch=true"]
    ng_dir = os.path.join('.', 'ng')
    install_path: str = os.path.abspath(ng_dir)
    kwargs: dict[str, str] = {'cwd': install_path}
    npm_runner = NpmRunner(settings)
    npm_args = ["install"]
    npm_runner.runshell(*npm_args, **kwargs)
    ng_runner = NgRunner(settings)
    ng_runner.runshell(*args, **kwargs)
