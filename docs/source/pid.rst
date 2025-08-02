Pid
===

.. currentmodule:: kcode.utils.pid

Create pid files
----------------

To create PID files, use the ``create_pid_file(name, quantity)`` method:

- ``name`` – a unique identifier for the PID file set.
- ``quantity`` – the maximum number of allowed PID files.

.. code-block:: python

   from kcode.utils.pid import Pid

   Pid("app_name", quantity=2).create_pid_file()


Get pid files
-------------

To retrieve a list of PID files, use the ``get_pid_files()`` method.

.. code-block:: python

   from kcode.utils.pid import Pid

   Pid("app_name").get_pid_files()


Delete pid files
----------------

To delete PID files, use the ``delete_pid_files(pid_files)`` method, where `pid_files` is a list returned from `get_pid_files()`.

.. code-block:: python

   from kcode.utils.pid import Pid

   pid_files = Pid("app_name").get_pid_files()
   Pid("app_name").delete_pid_files(pid_files)


Check if pid exists
-------------------

To check whether a process is running, use the static method ``Pid.check(pid)``.

.. code-block:: python

   from kcode.utils.pid import Pid

   Pid.check(12345)


Kill process
------------

To kill a process by PID, use the static method ``Pid.kill(pid)``.

.. code-block:: python

   from kcode.utils.pid import Pid

   Pid.kill(12345)
