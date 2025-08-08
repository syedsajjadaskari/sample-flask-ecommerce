import os
from Market import app, db

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    print("Database tables created/verified successfully")

# For Elastic Beanstalk, the application object should be called 'application'
application = app

if __name__ == "__main__":
    # Local development
    application.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))