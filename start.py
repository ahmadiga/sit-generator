import os
from subprocess import call

venvs = raw_input("Enter Virtual environments directory (default:~/venvs/): ") or "~/venv/"
project_name = raw_input("Enter project name (default:nameless): ") or "nameless"
venvs = os.path.expanduser(venvs)
if not os.path.exists(venvs):
    os.makedirs(venvs)

call(["virtualenv", os.path.join(venvs, project_name)])

project_path = os.path.join(venvs, project_name, "project")
if not os.path.exists(project_path):
    os.makedirs(project_path)
call(["wget", "https://github.com/ahmadiga/django_base/archive/0.0.1.tar.gz"])
call(["tar", "xvzf", "0.0.1.tar.gz", "-C", project_path])
call(["rm", "0.0.1.tar.gz"])

os.rename(os.path.join(project_path, "django_base-0.0.1"), os.path.join(project_path, project_name))
project_path = os.path.join(project_path, project_name)
