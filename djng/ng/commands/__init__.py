'''
ng cli documentation is at:
https://angular.dev/cli
'''

from .new_project import new_project
from .gen_application import gen_application
from .ng_build import ng_build

__all__ = ["ng_build", "gen_application", "new_project"]
