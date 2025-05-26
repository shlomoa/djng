'''
ng cli documentation is at:
https://angular.dev/cli
'''

from .ng_new import ng_new
from .ng_gen_app import ng_gen_app
from .ng_build import ng_build
from .ng_config import ng_config

__all__ = ["ng_build", "ng_gen_app", "ng_new", "ng_config"]
