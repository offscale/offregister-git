from sys import modules

from fabric.operations import sudo
from fabric.contrib.files import exists

from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.git import clone_or_update

from offregister_git import get_logger

logger = get_logger(modules[__name__].__name__)


def push0(**kwargs):
    apt_depends('git')

    destroy_node_modules = kwargs.get('destroy_node_modules', True)
    nm = '{}/{}'.format(kwargs['GIT_DIR'], 'node_modules')
    if not destroy_node_modules and exists(nm):
        sudo('cp -r "{nm}" /tmp/node_modules'.format(nm=nm))  # TODO: get new temp dir

    clone_or_update(repo=kwargs['GIT_REPO'], to_dir=kwargs['GIT_DIR'], use_sudo=kwargs.get('use_sudo', False),
                    branch=kwargs.get('GIT_BRANCH', 'master'), skip_reset=kwargs.get('skip_reset', False))
