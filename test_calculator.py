import unittest
from calculator import add

# Poorly written test suite
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # Correct test
    
    def test_empty(self):
        # Empty test method
        pass
    
    def test_bad_practice(self):
        # Assertion without proper message
        assert 1 + 1 == 2
