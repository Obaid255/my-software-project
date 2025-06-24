# app.py
def hello_world():
    print("Hello from the main branch, SPM Project!") # Keep this updated line

def login_user(username, password): # Keep the new function
    if username == "admin" and password == "password123":
        print(f"User {username} logged in successfully!")
        return True
    else:
        print("Invalid credentials.")
        return False

if __name__ == "__main__":
    hello_world()
    # login_user("admin", "password123") # Uncomment to test