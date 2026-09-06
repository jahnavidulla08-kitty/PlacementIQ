import urllib.request
import subprocess
import os
import sys

installer = os.path.expanduser(r'~\python_installer.exe')
target_dir = os.path.expanduser(r'~\python312')
url = 'https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe'

if not os.path.exists(os.path.join(target_dir, 'python.exe')):
    print('Downloading Python 3.12 installer...')
    urllib.request.urlretrieve(url, installer)
    print('Installing Python 3.12...')
    cmd = f'"{installer}" /quiet InstallAllUsers=0 TargetDir="{target_dir}" Include_pip=1 PrependPath=0 Shortcuts=0'
    res = subprocess.run(cmd, shell=True)
    print(f'Installer exited with code: {res.returncode}')
else:
    print('Python 3.12 already installed at', target_dir)
