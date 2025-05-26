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
    ng_dir = os.path.join('.', 'ng')
    install_path = os.path.abspath(ng_dir)
    kwargs = {
        'cwd': os.path.join(install_path),
        'shell': True
        }
    npm_runner = NpmRunner(settings)
    npm_args = ["install"]
    npm_kwargs: dict[str, str] = {'cwd': install_path}
    npm_runner.runshell(*npm_args, **npm_kwargs)
    ng_runner = NgRunner(settings)
    ng_runner.runshell(*args, **kwargs)
