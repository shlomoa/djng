""" ng runner """
import subprocess
import shutil

class BaseRunner:
    def __init__(self, basecmd, settings_dict):
        self.run_settings = settings_dict
        base_cmd_path = shutil.which(basecmd)
        if base_cmd_path is None:
            raise ChildProcessError("could not find ' + basecmd + ' executable")
        self.base_cmd_path: str = base_cmd_path

    def runshell(self, *args, **kwargs):
        """ng cli command runner"""        
        myargs = [self.base_cmd_path]
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
        myargs = [self.base_cmd_path]
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

class NpmRunner(BaseRunner):
    """A wrapper class for running npm cli"""
    def __init__(self, settings_dict):
        super().__init__('npm', settings_dict)

class NgRunner(BaseRunner):
    """A wrapper class for running ng cli"""
    def __init__(self, settings_dict):
        super().__init__('ng', settings_dict)
    
class NpxRunner(BaseRunner):
    """A wrapper class for running ng cli"""
    def __init__(self, settings_dict):
        super().__init__('npx', settings_dict)
