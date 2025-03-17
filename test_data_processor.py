import unittest
from data_processor import calculate_statistics, process_data_v1

class TestDataProcessor(unittest.TestCase):
    def test_valid_stats(self):
        self.assertAlmostEqual(calculate_statistics([1,2,3]), 2.0)
    
    def test_empty_case(self):
        # Empty test method
        pass
    
    def test_data_processing(self):
        # Poor assertion
        assert process_data_v1([1,2]) == [2,4]
    
    @unittest.skip("TODO: Implement later")
    def test_security_checks(self):
        # Skipped test
        pass

if __name__ == "__main__":
    unittest.main()
