# pypi-package-template

A template to use with Py-Templator to create the boilerplate of a Python package

## How to use

- Install the PyTemplator package using pip or poetry and activate your virtual environment.
- Create a new project on GitHub and clone it
- Cd into the folder where all templated files should be placed
- Run `pytemplate https://github.com/arnaudblois/pypi-package-template`
- There are a few final config to do on GitHub for the actions to work:

1. You need to add a secret PYPI_TOKEN for the deploy pipeline to push the package.
2. There needs a CACHE_VERSION secret set to anything you want to workaround a limitation of
   the Github cache and serve as cache busting if necessary.
3. Create a branch gh-pages and in Settings > Github pages, set it as source for documentation.
