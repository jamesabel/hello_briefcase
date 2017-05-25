
import os
import sysconfig
import _osx_support
import datetime
import site
import glob
import sys
from pprint import pprint

for m in [sysconfig, _osx_support]:
    for flag in ['SO', 'SOABI', 'EXT_SUFFIX']:
        cv = sysconfig.get_config_vars()
        print('%s : %s : %s' % (m.__name__, flag, cv[flag]))
print('sys.abiflags : %s' % sys.abiflags)
print('sitepackages *.so files:')

site_packages_roots = site.getsitepackages()
# special place for briefcase
site_packages_roots.append(os.path.join(site_packages_roots[0], '..', '..', '..', '..', 'app_packages'))
for site_packages_root in site_packages_roots:
    glob_path = os.path.abspath(os.path.join(site_packages_root, '*.so'))
    path_list = glob.glob(glob_path, recursive=True)
    if len(path_list) > 0:
        print('glob : %s' % glob_path)
        pprint(path_list)

import cryptography.fernet

# this is the error I get:
#Traceback (most recent call last):
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/python/lib/python3.5/runpy.py", line 193, in _run_module_as_main
#    "__main__", mod_spec)
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/python/lib/python3.5/runpy.py", line 85, in _run_code
#    exec(code, run_globals)
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/app/hello_briefcase/__main__.py", line 1, in <module>
#    from hello_briefcase.app import main
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/app/hello_briefcase/app.py", line 5, in <module>
#    import cryptography.fernet
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/app_packages/cryptography/fernet.py", line 17, in <module>
#    from cryptography.hazmat.primitives import hashes, padding
#  File "/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/macOS/hello_briefcase.app/Contents/Resources/app_packages/cryptography/hazmat/primitives/padding.py", line 13, in <module>
#    from cryptography.hazmat.bindings._padding import lib
#ImportError: No module named '_cffi_backend'


class HelloBriefcase:
    def main_loop(self):
        file_path = '/Users/james/projects/pycon_projects/hello_briefcase/hello_briefcase/hello_briefcase.txt'
        out = ['hello briefcase!!!', str(datetime.datetime.now()), file_path]
        with open(file_path, 'w') as f:
            for s in out:
                f.write(s)
                f.write('\n')
                print(s)


def main():
    # briefcase requires an instantiation of a class that has a main_loop() method
    hello = HelloBriefcase()
    return hello
