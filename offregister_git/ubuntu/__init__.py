from sys import modules

from offregister_fab_utils.apt import apt_depends
from offregister_fab_utils.git import clone_or_update

from offregister_git import get_logger

logger = get_logger(modules[__name__].__name__)


def push0(**kwargs):
    apt_depends('git')

    clone_or_update(repo=kwargs['GIT_REPO'], to_dir=kwargs['GIT_DIR'],
                    use_sudo=kwargs.get('use_sudo', False),
                    branch=kwargs.get('GIT_BRANCH', 'master'),
                    skip_reset=kwargs.get('skip_reset', False),
                    skip_clean=kwargs.get('skip_clean', True),
                    reset_to_first=kwargs.get('GIT_RESET_TO_FIRST', False))
