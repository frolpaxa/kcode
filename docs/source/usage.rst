Usage
=====

.. _installation:

Installation
------------

To use kcode, first install it using pip:

.. code-block:: console

   (.venv) $ pip install kcode

Create pid files
----------------

To create pid,
you can use the ``create_pid_file(:name, :quantity)`` function:

The ``name`` parameter sets a unique name.
The ``quantity`` parameter limits the number of instances created.

.. autofunction:: kcode.utils.pid

For example:

>>> from kcode.utils.pid import Pid
>>> Pid('app_name', quantity=2).create_pid_file()
(2740, '/tmp/app_name.pid.02e6c8b3-f6c3-4be9-b741-682c56283731')


Get pid files
----------------

To retrieve a list of pid files,
you can use the ``get_pid_files()`` function:

.. autofunction:: kcode.utils.pid

For example:

>>> from kcode.utils.pid import Pid
>>> Pid('app_name').get_pid_files()
[{'pid': 3634, 'file': '/tmp/app_name.pid.4651f1b5-b438-4f5d-bf3d-257c6e5c5228'}]


Delete pid files
----------------

To delete a pid files,
you can use the ``delete_pid_files(:pid_files)`` function:

The ``pid_files`` parameter list of received files ``get_pid_files()``.

.. autofunction:: kcode.utils.pid

For example:

>>> from kcode.utils.pid import Pid
>>> Pid('app_name').delete_pid_files(Pid('app_name').get_pid_files())
[{'pid': 2740, 'file': '/tmp/app_name.pid.02e6c8b3-f6c3-4be9-b741-682c56283731'}]


Check pid exists
----------------

To check existing pid,
you can use the ``check(:pid)`` function:

The ``pid`` parameter is a process id.

.. autofunction:: kcode.utils.pid

For example:

>>> from kcode.utils.pid import Pid
>>> Pid(None).check(:pid)
Killed

Kill process
----------------

To kill pid,
you can use the ``kill(:pid)`` function:

The ``pid`` parameter is a process id.

.. autofunction:: kcode.utils.pid

For example:

>>> from kcode.utils.pid import Pid
>>> Pid(None).kill(:pid)
Killed
