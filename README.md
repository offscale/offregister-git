offregister_git
===============
This package follows the offregister specification to get from `git`.

## Install dependencies

    pip install -r requirements.txt

## Install package

    pip install .

## Example use in offregister JSON

    {
        "module": "offregister-git",
        "kwargs": {
          "GIT_REPO": "https://github.com/offscale/offregister-app-push",
          "GIT_BRANCH": "trunk",
          "GIT_DIR": "/cool_location"
          "skip_reset": false,
          "use_sudo": true
        },
        "type": "fabric"
    }
