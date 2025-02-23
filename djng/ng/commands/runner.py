""" ng runner """
import subprocess
import shutil

class NgRunner:
    """A wrapper class for running ng cli"""

    def __init__(self, settings_dict):
        self.run_settings = settings_dict
        ng_path = shutil.which('ng')
        if ng_path is None:
            raise ChildProcessError("could not find ng executable")
        self.ng_cmd_path: str = ng_path

    def runshell(self, *args, **kwargs):
        """ng cli command runner"""        
        args = [self.ng_cmd_path] + list(args)
        cwd = None
        if 'cwd' in kwargs:
            cwd = kwargs['cwd']
        return subprocess.run(args, check=True, cwd=cwd)
