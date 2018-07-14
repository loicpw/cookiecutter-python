{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}  

|license| |python version| |build-status| |docs| |coverage| |pypi package|

.. |license| image:: https://img.shields.io/github/license/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}.svg
.. |build-status| image:: https://travis-ci.org/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}.svg?branch=master
    :target: https://travis-ci.org/{{cookiecutter.author_username }}/{{ cookiecutter.package_name }}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.package_name }}/badge/?version=latest
    :target: http://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |coverage| image:: https://coveralls.io/repos/github/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}/badge.svg?branch=master
    :target: https://coveralls.io/github/{{ cookiecutter.author_username }}/{{ cookiecutter.package_name }}?branch=master
.. |pypi package| image:: https://badge.fury.io/py/{{ cookiecutter.package_name }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.package_name }}
.. |python version| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.package_name }}

{{ cookiecutter.package_description }}

install and test
=======================

install from pypi
********************

using pip:

.. code-block:: bash

    $ pip install {{ cookiecutter.package_name }}

production install
******************

There is a makefile in the project root directory:
    
.. code-block:: bash

    $ make install

Using pip, the above is equivalent to:

.. code-block:: bash

    $ pip install -r requirements.txt                                             
    $ pip install -e .

dev install
****************

There is a makefile in the project root directory:
    
.. code-block:: bash

    $ make dev

Using pip, the above is equivalent to:

.. code-block:: bash

    $ pip install -r requirements-dev.txt                                             
    $ pip install -e .

run the tests
******************

Use the makefile in the project root directory:

.. code-block:: bash

    $ make test

This runs the tests generating a coverage html report

build the doc
******************

The documentation is made with sphinx, you can use the makefile in the
project root directory to build html doc:

.. code-block:: bash

    $ make doc

Documentation
=======================

Documentation on `Read The Docs`_.

Meta
=======================

{{ cookiecutter.author_username }} - {{ cookiecutter.author_email }}

Distributed under the MIT license. See ``LICENSE.txt`` for more information.

{{ cookiecutter.author_github }}


.. _Read The Docs: http://{{ cookiecutter.package_name }}.readthedocs.io/en/latest/

