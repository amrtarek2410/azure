# Unused import
import csv

# Hardcoded credentials (security hotspot)
ADMIN_PASSWORD = "super_secret_123"

# Unused variable
CONFIG_OPTIONS = {"timeout": 30}

# Duplicated code
def calculate_age_v1(birth_year):
    return 2023 - birth_year

def calculate_age_v2(birth_year):  # Duplicate of v1
    return 2023 - birth_year

# Inconsistent naming
def fetch_user_data(userID):  # camelCase parameter
    return {"id": userID, "name": "Test User"}

# Unreachable code
def deprecated_method():
    print("This method is deprecated")
    return True
deprecated_method()
print("This line is unreachable")

# Potential NoneType error
def process_user_input(data):
    return data.strip().upper()  # No null check

# SQL injection vulnerability
def create_query(user_id):
    return f"SELECT * FROM users WHERE id = {user_id}"  # Security hotspot

# Poor error handling
def parse_integer(value):
    return int(value)  # Potential ValueError

if __name__ == "__main__":
    print(process_user_input(None))  # Will crash
    print(parse_integer("text"))  # Invalid conversion
    print(create_query("1 OR 1=1"))  # SQL injection demo
