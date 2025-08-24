from website import create_app, db
from website.models import User

# Use your existing app configuration
app = create_app()

with app.app_context():
    try:
        users = User.query.all()
        if users:
            print("\nRegistered Users:")
            print("-----------------")
            for user in users:
                print(f"Name: {user.first_name}, Email: {user.email}")
        else:
            print("No users found in the database.")
    except Exception as e:
        print(f"Error accessing database: {e}")
