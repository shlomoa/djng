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
        myargs = [self.ng_cmd_path]
        myargs += args
        cwd = None
        if ('cwd' in kwargs) and (kwargs['cwd'] is not None):
            cwd = kwargs['cwd']
        shell = False
        if ('shell' in kwargs) and (kwargs['shell'] is not None):
            shell = kwargs['shell']
        env = None
        if 'env' in kwargs:
            env = kwargs['env']
        print(myargs)
        return subprocess.run(myargs, check=True, cwd=cwd, shell=shell, env=env)

    def getfromshell(self, *args, **kwargs):
        """ng cli command runner, read output"""        
        myargs = [self.ng_cmd_path]
        myargs += args
        cwd = None
        if ('cwd' in kwargs) and (kwargs['cwd'] is not None):
            cwd = kwargs['cwd']
        shell = False
        if ('shell' in kwargs) and (kwargs['shell'] is not None):
            shell = kwargs['shell']
        env = None
        if 'env' in kwargs:
            env = kwargs['env']
        print(myargs)
        return subprocess.check_output(myargs, cwd=cwd, shell=shell, env=env)
