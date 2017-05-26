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

        compiled_ver = '%s%s' % (sys.version_info.major, sys.version_info.minor)
        compiled_ver_and_flag = '%s%s' % (compiled_ver, sys.abiflags)
        print('compiled_ver_and_flag : %s' % compiled_ver_and_flag)

        # look for all the package compile flags
        # example of a compiled binary filename:
        # _cffi_backend.cpython-35m-darwin.so

        for root, _, briefcase_files in os.walk('macOS'):
            for briefcase_file in briefcase_files:
                if 'app_packages' in root:
                    file_match = re.match('([\w_\.]*)(cpython-)(\d+)(\w*)(-darwin.so)', briefcase_file)
                    if file_match:
                        package_ver = file_match.group(3)
                        if compiled_ver != package_ver:
                            print('error : compiled and package versions are different (compiled : %s, package : %s)' %
                                  (compiled_ver, package_ver))
                        package_flag = file_match.group(4)
                        package_ver_and_flag = package_ver + package_flag
                        full_path = os.path.join(root, briefcase_file)
                        print('%s : package_ver_and_flag : %s' % (full_path, package_ver_and_flag))
                        if package_ver_and_flag != compiled_ver_and_flag:
                            # Found a mismatch - copy over the package's .so to a file name that the python interpreter
                            # is looking for.
                            fixup_path = os.path.join(root, briefcase_file.replace(package_ver_and_flag, compiled_ver_and_flag))
                            if not os.path.exists(fixup_path):
                                print('flag mismatch between python "%s" and package "%s" - fixing up' %
                                      (compiled_ver_and_flag, package_ver_and_flag))
                                print('copying %s to %s' % (full_path, fixup_path))
                                shutil.copy2(full_path, fixup_path)

if __name__ == '__main__':
    fixup()
