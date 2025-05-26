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
    config_key_value = options["attribute"]
    key,value = config_key_value.split('=')
    args += [key, value]
    ng_dir = os.path.abspath(os.path.join('.', 'ng'))
    npm_runner = NpmRunner(settings)
    kwargs: dict[str, str] = {'cwd': ng_dir}
    npm_args: list[str] = ["install"]
    npm_runner.runshell(*npm_args, **kwargs)
    ng_runner = NgRunner(settings)
    ng_runner.runshell(*args, **kwargs)
