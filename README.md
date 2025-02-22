# python-cli-template
Template for Python CLI apps

# Features
- CMD: build
- CMD: installation targets
  - venv/
  - user local bin/
  - TODO: global bin/
- CMD: CLI test
  - From venv/
  - From user local bin/
  - Dev mode
- CMD: lib test

# Uses
- [setuptools](https://setuptools.pypa.io/en/latest/index.html) package builder
- [Jinja](https://jinja.palletsprojects.com/en/stable/) template framework
- [tomli-w](https://pypi.org/project/tomli-w/) TOML writer

# Tested config
- FreeBSD w/ Python 3.11