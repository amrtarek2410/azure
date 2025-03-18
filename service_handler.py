import warnings
import hashlib

# Deprecated hashing method (SonarQube will flag as security hotspot)
def hash_password(password):
    # Deprecated: SHA-1 is insecure
    return hashlib.sha1(password.encode()).hexdigest()

# Unreliable division (potential ZeroDivisionError)
def calculate_ratio(a, b):
    return a / b  # No error handling

# Duplicated code block
def process_data_v1(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2)
    return result

# Duplicate of process_data_v1
def process_data_v2(data):
    result = []
    for item in data:
        if item % 2 == 0:
            result.append(item * 2)
    return result

# Deprecated warnings format
def legacy_warning():
    warnings.warn("This is deprecated", DeprecationWarning)  # Should use logging

# Unreliable type handling
def string_length(value):
    return len(value)  # Fails if value is None

# Deprecated string formatting
def old_format():
    return "%s %d" % ("test", 42)  # Should use f-strings

# Unreliable dictionary access
def get_value(data, key):
    return data[key]  # Potential KeyError

if __name__ == "__main__":
    print(calculate_ratio(10, 0))  # ZeroDivisionError
    print(string_length(None))     # TypeError
    print(get_value({}, "missing")) # KeyError
