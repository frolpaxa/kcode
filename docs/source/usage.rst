Usage
=====

.. _installation:

Installation
------------

To use kcode, first install it using pip:

.. code-block:: console

   (.venv) $ pip install kcode

.. currentmodule:: kcode.utils.pid

.. rubric:: Pid API

.. autoclass:: Pid
   :members: create_pid_file, get_pid_files, delete_pid_files, check, kill
   :undoc-members:
   :show-inheritance:

Create pid files
----------------

To create pid files,
you can use the ``create_pid_file(name, quantity)`` method of the `Pid` class:

- ``name`` sets a unique identifier.
- ``quantity`` limits the number of allowed instances.

**Example:**

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid("app_name", quantity=2).create_pid_file()


Get pid files
-------------

To retrieve a list of pid files,
use the ``get_pid_files()`` method:

**Example:**

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid("app_name").get_pid_files()


Delete pid files
----------------

To delete PID files,
use the ``delete_pid_files(pid_files)`` method, where `pid_files` is a list returned from `get_pid_files()`:

**Example:**

.. code-block:: python

   from kcode.utils.pid import Pid
   pid_instance = Pid("app_name")
   pid_files = pid_instance.get_pid_files()
   pid_instance.delete_pid_files(pid_files)


Check if pid exists
-------------------

To check whether a given process ID is alive,
use the static method ``Pid.check(pid)``:

**Example:**

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid.check(12345)


Kill process
------------

To kill a process by PID,
use the static method ``Pid.kill(pid)``:

**Example:**

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid.kill(12345)
