# Project Setup

Here we provide some details about the project setup. Most of the choices are explained in the
[guide](https://guide.esciencecenter.nl). Links to the relevant sections are included below. Feel free to remove this
text when the development of the software package takes off.

For a quick reference on software development, we refer to [the software guide
checklist](https://guide.esciencecenter.nl/#/best_practices/checklist).

## Version control

Once your Python package is created, put it under [version
control](https://guide.esciencecenter.nl/#/best_practices/version_control)! We recommend using
[git](http://git-scm.com/) and [github](https://github.com/).

```shell
cd justatest
git init
git add --all
git commit
```

To put your code on github, follow [this
tutorial](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).

## Python versions

This repository is set up with Python versions:

- 3.6
- 3.7
- 3.8
- 3.9

Add or remove Python versions based on project requirements. See [the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python) for more information about Python
versions.

## Package management and dependencies

You can use either pip or conda for installing dependencies and package management. This repository does not force you
to use one or the other, as project requirements differ. For advice on what to use, please check [the relevant section
of the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=dependencies-and-package-management).

-   Dependencies should be added to `setup.py` in the `install\_requires` list.

## Packaging/One command install

You can distribute your code using pipy or conda. Again, the project template does not enforce the use of either one.
[The guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code) can
help you decide which tool to use for packaging.

## Testing and code coverage

-   Tests should be put in the `tests` folder.
-   The `tests` folder contains:
    -   Example tests that you should replace with your own meaningful tests (file:
        `test_justatest`)
    -   A test that checks whether your code conforms to the Python style guide (PEP 8) (file: `test_lint.py`)
-   The testing framework used is [PyTest](https://pytest.org)
    -   [PyTest introduction](http://pythontesting.net/framework/pytest/pytest-introduction/)
-   Tests can be run with `python setup.py test`
    -   This is configured in `setup.py` and `setup.cfg`
-   Use [Travis CI](https://travis-ci.com/) to automatically run tests and to test using multiple Python versions
    -   Configuration can be found in `.travis.yml`
    -   [Getting started with Travis
        CI](https://docs.travis-ci.com/user/getting-started/)
-   [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=testing)

## Documentation

-   Documentation should be put in the `docs` folder. The contents have
    been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
-   We recommend writing the documentation using Restructured Text
    (reST) and Google style docstrings.
    -   [Restructured Text (reST) and Sphinx
        CheatSheet](http://openalea.gforge.inria.fr/doc/openalea/doc/_build/html/source/sphinx/rest_syntax.html)
    -   [Google style docstring
        examples](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
-   The documentation is set up with the Read the Docs Sphinx Theme.
    -   Check out the [configuration
        options](https://sphinx-rtd-theme.readthedocs.io/en/latest/).
-   To generate html documentation run `python setup.py build_sphinx`
    -   This is configured in `setup.cfg`
    -   Alternatively, run `make html` in the `docs` folder.
-   The `docs/_templates` directory contains an (empty) `.gitignore`
    file, to be able to add it to the repository. This file can be
    safely removed (or you can just leave it there).
-   To put the documentation on [Read the
    Docs](https://readthedocs.org), log in to your Read the Docs
    account, and import the repository (under 'My Projects').
    -   Include the link to the documentation in this [README]().
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=writingdocumentation)

## Coding style conventions and code quality

-   Check your code style with `prospector`
-   You may need run `pip install .[dev]` first, to install the required
    dependencies
-   You can use `yapf` to fix the readability of your code style and
    `isort` to format and group your imports
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=coding-style-conventions)

## Continuous code quality

-   [Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report on each push
-   The GitHub organization and repository must be added Sonarcloud for analysis to work by going to
    [Sonarcloud](https://sonarcloud.io/projects/create), login with your GitHub account,
    add organization or reuse existing and setup repository
-   Analysis is run in [GH action workflow](.github/workflows/quality.yml)
-   To run analysis a token must be created at [Sonarcloud account](https://sonarcloud.io/account/security/)
    and token must be added as `SONAR_TOKEN` to [secrets on GitHub](https://github.com/sverhoeven/justatest/settings/secrets/actions)

## Package version number

-   We recommend using [semantic
    versioning](https://guide.esciencecenter.nl/#/best_practices/releases?id=semantic-versioning).
-   For convenience, the package version is stored in a single place:
    `justatest/__version__.py`. For updating the
    version number, you only have to change this file.
-   Don't forget to update the version number before [making a
    release](https://guide.esciencecenter.nl/#/best_practices/releases)!

## Logging

-   We recommend using the logging module for getting useful information
    from your module (instead of using print).
-   The project is set up with a logging example.
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=logging)

## CHANGELOG.rst

-   Document changes to your software package
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/releases?id=changelogmd)
           

## CITATION.cff

-   To allow others to cite your software, add a `CITATION.cff` file
-   It only makes sense to do this once there is something to cite
    (e.g., a software release with a DOI).
-   Follow the [making software
    citable](https://guide.esciencecenter.nl/#/citable_software/making_software_citable)
    section in the guide.

## CODE\_OF\_CONDUCT.rst

-   Information about how to behave professionally
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=code-of-conduct)

## CONTRIBUTING.rst

-   Information about how to contribute to this software package
-   [Relevant section in the
    guide](https://guide.esciencecenter.nl/#/best_practices/documentation?id=contribution-guidelines)

## MANIFEST.in

-   List non-Python files that should be included in a source distribution
-   [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=building-and-packaging-code)

## NOTICE

-   List of attributions of this project and Apache-license dependencies
-   [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/licensing?id=notice)
