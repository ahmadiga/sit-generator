from tempfile import mkstemp
from shutil import move

import os
from os import remove, close

from os import makedirs, rename

from os.path import join, expanduser, isfile, exists
from subprocess import call


def replace_djang_base(path, project_name):
    for dirname in os.listdir(path):
        if isfile(join(path, dirname)):
            replace(join(path, dirname), "django_base", project_name)
        else:
            replace_djang_base(join(path, dirname), project_name)


def replace(file_path, pattern, subst):
    # Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path, 'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    close(fh)
    # Remove original file
    remove(file_path)
    # Move new file
    move(abs_path, file_path)


virtualenvs_path = "/venv/"
project_name = "sitbase"
virtualenvs_path = expanduser(virtualenvs_path)
if not exists(virtualenvs_path):
    makedirs(virtualenvs_path)

call(["virtualenv", join(virtualenvs_path, project_name)])

project_path = join(virtualenvs_path, project_name, "project")
if not exists(project_path):
    makedirs(project_path)
call(["wget", "https://github.com/ahmadiga/django_base/archive/0.0.1.tar.gz"])
call(["tar", "xvzf", "0.0.1.tar.gz", "-C", project_path])
call(["rm", "0.0.1.tar.gz"])

rename(join(project_path, "django_base-0.0.1"), join(project_path, project_name))
project_path = join(project_path, project_name)
rename(join(project_path, "django_base"), join(project_path, project_name))
call([join(virtualenvs_path, project_name, "bin/pip"), "install", "-r",
      join(project_path, "requirements.txt")])
replace_djang_base(project_path, project_name)
call([join(virtualenvs_path, project_name, "bin/python"), join(project_path, "manage.py"), "bower_install"])
call([join(virtualenvs_path, project_name, "bin/python"), join(project_path, "manage.py"), "migrate"])
