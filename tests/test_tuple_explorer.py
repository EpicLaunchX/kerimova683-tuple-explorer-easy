import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../.github')))
from tuple_explorer import get_items

import unittest
from unittest.mock import patch

class TestGetItems(unittest.TestCase):
    @patch('builtins.input', return_value="apple,banana,orange")
    def test_get_items(self, mock_input):
        result = get_items()
        expected = ("apple", "banana", "orange")
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()