

import subprocess

def git():
    a="clone", "https://github.com/OpenNI/OpenNI.git"
    return subprocess.check_call(['git'] + list(a))

git()

