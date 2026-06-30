from app import app, db, Other
import bcrypt

def create_admin():
    with app.app_context():
        # Check if admin already exists
        if not Other.query.filter_by(email="admin@mail.com").first():
            admin = Other(
                name="AdminUser",
                role="admin",
                email="admin@mail.com",
                password="admin123"  # constructor hashes automatically
            )
            db.session.add(admin)
            db.session.commit()
            print("Admin created!")
        else:
            print("Admin already exists.")

if __name__ == "__main__":
    create_admin()
