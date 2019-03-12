Personal `cookiecutter`_ package for github python projects
=====================================================================

This is my simple `cookiecutter`_ for creating python projects, it uses:

- MIT license
- **AUTHORS**, **README**, **HISTORY** **.rst** files
- **requirements.txt** and **requirements-dev.txt** files
- sphinx doc with `Read The Docs`_ theme
- automated tests with `Travis CI`_
- tests using `pytest`_
- `coveralls`_
- pep8 test
- badges in README file
- **makefile** with targets: **dev**, **test**, **doc**
- additional **makefile** targets: **freeze** (sorted pip freeze), **find-version** (find version statements in repos)

Usage
-----

.. code-block:: bash 

    $ pip install cookiecutter
    $ cookiecutter https://github.com/loicpw/cookiecutter-python.git

.. _cookiecutter: https://cookiecutter.readthedocs.io
.. _Read The Docs: https://readthedocs.org
.. _Travis CI: https://travis-ci.org
.. _pytest: https://docs.pytest.org/en/latest/
.. _coveralls: https://coveralls.io
