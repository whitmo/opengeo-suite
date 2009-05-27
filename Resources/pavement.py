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

from paver import setuputils
from paver.easy import *
from paver.easy import call_task #debug,
from paver.easy import cmdopts #,consume_args
from paver.easy import path, sh, info, pushd
from paver.easy import task, options, Bunch
from paver.setuputils import setup
from paver.tasks import help, needs
from setuptools import find_packages
import pkg_resources
import os
import re
import shutil
import subprocess
import getpass
import pwd
import pip
import tempita

version = "0.0"

curdir = os.path.abspath(os.curdir)

options(
    virtualenv=Bunch(script_name="build_app",
                     #packages_to_install=['supervisor',
                     #                     'tempita',
                     #                     'paste',
                     #                     'jstools'],
                     paver_command_line="after_bootstrap"
                     ),
#    sphinx=Bunch(docroot="src/trunk/docsrc",
#                 builddir=path(curdir) / "built")
    )
