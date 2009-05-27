# build file for application
"""
things to setup
* sfb for geoexplorer
* proxy???
* geoserver
* application js
"""

# requires python 2.5
from __future__ import with_statement

try:
    from paver.virtual import bootstrap
except :
    # minilib does not support bootstrap
    pass

from ConfigParser import ConfigParser
from paver import setuputils
from paver.easy import *
from paver.easy import call_task #debug,
from paver.easy import cmdopts #,consume_args
from paver.easy import path, sh, info, pushd
from paver.easy import task, options, Bunch
from paver.setuputils import setup
from paver.tasks import help, needs
from setuptools import find_packages
import getpass
import os
import pkg_resources
import pwd
import re
import shutil
import subprocess


version = "0.0"

curdir = os.path.abspath(os.curdir)

options(
    virtualenv=Bunch(script_name="build_app_env",
                     #packages_to_install=['supervisor',
                     #                     'tempita',
                     #                     'paste',
                     #                     'jstools'],
                     paver_command_line="after_bootstrap"
                     ),
               #    sphinx=Bunch(docroot="src/trunk/docsrc",
               #                 builddir=path(curdir) / "built")
    )

APPCONF = "app-conf.cfg"
_DIRS = "src", "var", "etc", "var/logs", "usr",

@task
def auto(default_conf=APPCONF):
    env = os.environ.get('VIRTUAL_ENV')
    if env is None:
        env = path("./").abspath()

    cp = ConfigParser()
    cp.read(default_conf)
    options(config=cp,
            env=env,
            conf_fp=default_conf)


@task
@needs(['auto'])
def after_bootstrap():
    call_task("dir_layout")


@task
def dir_layout():
    env = path(options.env)
    for p in _DIRS:
        if not (env / p).exists():
            os.mkdir(env / p)

# 0. install py packages

# 1.
# setup supervisor
# setup proxy
# setup geoserver

# 2.
# ui for finding data
# ui for starting and restart processes
# geoexplorer

# 3.
# geobuilder

# 4.
# postgis of love

