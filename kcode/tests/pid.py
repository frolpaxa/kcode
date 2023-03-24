import unittest

from kcode.utils.pid import Pid


class PidTestCase(unittest.TestCase):
    def setUp(self):
        self.test = Pid("test", quantity=4)

    def tearDown(self):
        pass

    def test_check(self):
        pid, _ = self.test.create_pid_file()
        self.assertTrue(self.test.check(pid))

    def test_get_pid_files(self):
        self.assertTrue(len(self.test.get_pid_files()) == 1)

    def test_quantity(self):
        for _ in range(self.test.quantity * 2):
            self.test.create_pid_file()

        self.assertTrue(len(self.test.get_pid_files()) <= self.test.quantity)


if __name__ == "__main__":
    unittest.main()
