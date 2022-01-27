.. highlight:: shell

============
Installation
============


Stable release
--------------

You can either add {{ pypi_name }} to your project using `Poetry`_ or inside a virtual
environment by using pip:

.. code-block:: console

    $ poetry add {{ pypi_name }}
    # or
    $ pip install {{ pypi_name }}



If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _Poetry: https://python-poetry.org/
.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ pypi_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone {{ git_url }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL {{ git_url }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: {{ git_url }}
.. _tarball: {{ git_url }}/tarball/master
