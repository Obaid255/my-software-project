# app.py
def hello_world():
    print("Hello, SPM Project!")

def login_user(username, password):
    if username == "admin" and password == "password123":
        print(f"User {username} logged in successfully!")
        return True
    else:
        print("Invalid credentials.")
        return False

if __name__ == "__main__":
    hello_world()
    # login_user("admin", "password123") # Uncomment to test