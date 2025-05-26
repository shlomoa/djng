"""
    ng_openapi_gen generated TS data model from open API schema file
    Documentation is at: https://www.npmjs.com/package/ng-openapi-gen
"""

import os
from django.conf import settings
from .runner import NpmRunner, NpxRunner


def ng_openapi_gen(**options):
    """
    Example command:
    npx c --input ../schema.yml --output quetionaire/src/app/openapi
    """
    args: list[str] = ["ng-openapi-gen"]    
    if "input" in options and options['input'] is not None:
        args += ["--input", options["input"]]
    if "output" in options and options["output"] is not None:
        args += ["--output", options["output"]]
    ng_dir = os.path.join('.', 'ng')
    install_path: str = os.path.abspath(ng_dir)
    kwargs: dict[str, str] = {'cwd': install_path}
    npm_runner = NpmRunner(settings)
    npm_args = ["install"]
    npm_runner.runshell(*npm_args, **kwargs)
    npm_args += ['ng-openapi-gen']
    npm_runner.runshell(*npm_args, **kwargs)
    npx_runner = NpxRunner(settings)
    npx_runner.runshell(*args, **kwargs)
