import psycopg2
import os

# Hardcoded credentials (security hotspot)
DB_CONFIG = {
    "host": "localhost",
    "database": "testdb",
    "user": "admin",
    "password": "super_secret_123"  # SonarQube will flag this
}

# SQL injection vulnerability
def get_user_data(username):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    # UNSAFE: Concatenated SQL query
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")  # SonarQube will flag
    result = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return result

# Connection leak potential
def update_user_email(user_id, new_email):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    try:
        cursor.execute("UPDATE users SET email = %s WHERE id = %s", (new_email, user_id))
        conn.commit()
    except Exception as e:  # Too broad exception
        print(f"Error: {e}")
    # Missing finally block to close resources
    
# No error handling for connection failures
def get_all_users():
    conn = psycopg2.connect(**DB_CONFIG)  # No try/catch
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

if __name__ == "__main__":
    # Demo insecure usage
    print(get_user_data("admin' OR 1=1 --"))  # SQL injection example
    print(get_all_users())
