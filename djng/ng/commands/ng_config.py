"""
    ng generate application
    Documentation is at: https://angular.dev/cli/generate/application
"""

import os
from django.conf import settings
from .runner import NgRunner, NpmRunner


def ng_config(**options):
    """
    Example command:
    ng config projects.questionaire.architect.build.options.outputPath
    """
    args: list[str] = ["config"]
    config_key = options["attribute"]
    args += [config_key]
    ng_dir = os.path.abspath(os.path.join('.', 'ng'))
    kwargs = {
        'cwd': ng_dir,
        'shell': True
        }
    npm_runner = NpmRunner(settings)
    npm_kwargs: dict[str, str] = {'cwd': ng_dir}
    npm_args: list[str] = ["install"]
    npm_runner.runshell(*npm_args, **npm_kwargs)
    ng_runner = NgRunner(settings)
    ng_runner.runshell(*args, **kwargs)
