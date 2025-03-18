import unittest
from user_manager import calculate_age_v1, fetch_user_data

class TestUserManager(unittest.TestCase):
    def test_valid_age(self):
        self.assertEqual(calculate_age_v1(2000), 23)  # Correct test
    
    def test_empty_case(self):
        # Empty test method
        pass
    
    def test_bad_assertion(self):
        # Assertion without message
        assert fetch_user_data("123")["name"] == "Test User"
    
    @unittest.skip("TODO: Implement security tests")
    def test_security_checks(self):
        # Skipped test
        pass

if __name__ == "__main__":
    unittest.main()
