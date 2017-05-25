import sys
import os
import re
import shutil

def fixup():
    """
    workaround for https://github.com/pybee/briefcase/issues/44
    see https://www.python.org/dev/peps/pep-3149/ for the meaning of the flags    
    :return: 
    """

    if sys.platform == 'darwin':
        # OSX/MacOS

        compiled_ver_and_flag = '%s%s%s' % (sys.version_info.major, sys.version_info.minor, sys.abiflags)
        print('compiled_ver_and_flag : %s' % compiled_ver_and_flag)

        # look for all the package compile flags
        # _cffi_backend.cpython-35m-darwin.so

        for root, dirs, files in os.walk(os.path.join('macOS', '')):
            for file in files:
                if 'app_packages' in root:
                    result = re.match('([\w_\.]*)(cpython-)([\d\w]+)(-darwin.so)', file)
                    if result:
                        package_ver_and_flag = result.group(3)
                        full_path = os.path.join(root, file)
                        print('%s : package_ver_and_flag : %s' % (full_path, package_ver_and_flag))
                        if package_ver_and_flag != compiled_ver_and_flag:
                            print('flag mismatch between python "%s" and package "%s" - fixing up' %
                                  (compiled_ver_and_flag, package_ver_and_flag))
                            fixup_path = os.path.join(root, file.replace(result.group(3), compiled_ver_and_flag))
                            print('copying %s to %s' % (full_path, fixup_path))
                            shutil.copy2(full_path, fixup_path)

if __name__ == '__main__':
    fixup()
