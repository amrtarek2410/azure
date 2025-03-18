import unittest
from service_handler import calculate_ratio, process_data_v1

class TestServiceHandler(unittest.TestCase):
    # Unreliable test (no exception handling)
    def test_ratio(self):
        self.assertEqual(calculate_ratio(4, 2), 2)
    
    # Duplicated test logic
    def test_process_data_v1(self):
        self.assertEqual(process_data_v1([1,2,3]), [4])
    
    def test_process_data_v2(self):  # Duplicate of v1 test
        self.assertEqual(process_data_v1([1,2,3]), [4])
    
    # Deprecated test naming
    def testOldFormat(self):  # Should use snake_case
        pass
    
    # Unreliable assertion
    def test_length(self):
        assert len("test") == 4  # Bare assert

if __name__ == "__main__":
    unittest.main()
