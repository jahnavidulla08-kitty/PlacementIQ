import urllib.request
import zipfile
import os
import subprocess
import sys

tools_dir = os.path.expanduser(r'~\tools')
os.makedirs(tools_dir, exist_ok=True)
uv_zip = os.path.join(tools_dir, 'uv.zip')
uv_exe = os.path.join(tools_dir, 'uv.exe')

if not os.path.exists(uv_exe):
    print("Downloading Astral uv binary...")
    url = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
    urllib.request.urlretrieve(url, uv_zip)
    print("Extracting uv...")
    with zipfile.ZipFile(uv_zip, 'r') as z:
        z.extractall(tools_dir)
    print("uv extracted successfully!")
else:
    print("uv already exists!")

# Now create a python 3.12 venv in the project directory
project_dir = r"c:\Users\potal\OneDrive\Desktop\project"
venv_dir = os.path.join(project_dir, ".venv")

print("Creating Python 3.12 virtual environment using uv...")
cmd = f'"{uv_exe}" venv "{venv_dir}" --python 3.12'
res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("uv venv output:", res.stdout, res.stderr)

print("Installing all required packages into .venv...")
cmd_install = f'"{uv_exe}" pip install --venv "{venv_dir}" fastapi uvicorn sqlalchemy pydantic pandas numpy scikit-learn joblib'
res_install = subprocess.run(cmd_install, shell=True, capture_output=True, text=True)
print("uv pip install output:", res_install.stdout, res_install.stderr)
print("Environment setup completed!")
