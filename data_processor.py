# Unused import
import json

# Hardcoded credentials (security hotspot)
API_KEY = "sk_live_1234567890abcdefghijklmnop"

# Unused variable
CONFIG_SETTINGS = {"timeout": 30}

# Function with potential division by zero
def calculate_statistics(numbers):
    total = sum(numbers)
    return total / len(numbers)  # Possible ZeroDivisionError

# Duplicated code (code smell)
def process_data_v1(data):
    return [x * 2 for x in data]

def process_data_v2(data):
    return [x * 2 for x in data]  # Duplicate of v1

# Inconsistent naming
def fetch_user_info(userId):  # camelCase
    return {"id": userId, "name": "Test User"}

# Unreachable code
def deprecated_method():
    print("This method is no longer used")
    return True
deprecated_method()
print("This message is unreachable")

# SQL injection vulnerability
def get_user_query(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Security hotspot
    return query

# Poor error handling
def parse_value(value):
    return int(value)  # Potential ValueError

# Unused function
def helper_method():
    pass

if __name__ == "__main__":
    # Demonstrate issues
    print(calculate_statistics([]))  # Empty list
    print(parse_value("text"))  # Invalid conversion
    print(get_user_query("1 OR 1=1"))  # SQL injection demo
