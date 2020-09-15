offregister_git
===============
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech)
![Python version range](https://img.shields.io/badge/python-2.7%20|%203.4%20|%203.5%20|%203.6%20|%203.7%20|%203.8-blue.svg)
[![License](https://img.shields.io/badge/license-Apache--2.0%20OR%20MIT-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

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
## License

Licensed under either of

- Apache License, Version 2.0 ([LICENSE-APACHE](LICENSE-APACHE) or <https://www.apache.org/licenses/LICENSE-2.0>)
- MIT license ([LICENSE-MIT](LICENSE-MIT) or <https://opensource.org/licenses/MIT>)

at your option.

### Contribution

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in the work by you, as defined in the Apache-2.0 license, shall be
dual licensed as above, without any additional terms or conditions.
