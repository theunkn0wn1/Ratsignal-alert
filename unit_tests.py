import unittest
import alert
from utils.playground.shared_resources import CommandBase
"""
Unit Test file.
"""
class alertTests(unittest.TestCase):
    def test_startup(self):
        pass


class CommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        alert.init()

    def test_init(self):
        expected_commands = [
            'help',

        ]
        for command in expected_commands:
            with self.subTest(command = command):
                self.assertIsNotNone(CommandBase.getCommand(command))
if __name__ == "__main__":
    unittest.main()
