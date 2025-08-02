Pid
===

.. currentmodule:: kcode.utils.pid

Create pid files
----------------

To create pid files, use the ``create_pid_file(name, quantity)`` method:

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid("app_name", quantity=2).create_pid_file()

Get pid files
-------------

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid("app_name").get_pid_files()

Delete pid files
----------------

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid("app_name").delete_pid_files(pid_files)

Check if pid exists
-------------------

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid.check(12345)

Kill process
------------

.. code-block:: python

   from kcode.utils.pid import Pid
   Pid.kill(12345)
