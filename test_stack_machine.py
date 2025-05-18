import unittest
from unittest.mock import patch
from io import StringIO
from stack_machine import StackMachine

class TestStackMachine(unittest.TestCase):
    def setUp(self):
        self.stack = StackMachine()

    def test_push_and_top(self):
        self.stack.push(10)
        self.assertEqual(self.stack.top(), 10)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), -1)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_empty(self):
        self.assertEqual(self.stack.empty(), 1)
        self.stack.push(1)
        self.assertEqual(self.stack.empty(), 0)

    def test_top_empty(self):
        self.assertEqual(self.stack.top(), -1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mocked_output(self, mock_stdout):
        self.stack.push(5)
        self.stack.push(6)
        print(self.stack.top())
        print(self.stack.pop())
        print(self.stack.pop())
        print(self.stack.pop())

        expected_output = "6\n6\n5\n-1\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
