import sys
import os
sys.path.append(os.path.dirname(__file__)+'/..')
from website import create_app,db # Assuming create_app is a function in __init__.py that initializes your Flask app
from website.models import User, PersonalityProfile, UserPreferences
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

app = create_app() 
fake = Faker()

def create_fake_data():
    with app.app_context():
        for _ in range(100):
            # Create fake user data
            email = fake.email()
            user_name = fake.user_name()
            password = fake.password()  # Consider hashing this password before production use
            # Assign a random budget category
            new_user = User(
                email=email,
                user_name=user_name,
                password=generate_password_hash(password, method='pbkdf2:sha256'),
            )
            db.session.add(new_user)

            # Create a personality profile
            new_profile = PersonalityProfile(
                user=new_user,
                age=random.randint(18, 75),
                budget= random.randint(1,3),
                openness=random.randint(1, 5),
                conscientiousness=random.randint(1, 5),
                extraversion=random.randint(1, 5),
                agreeableness=random.randint(1, 5),
                neuroticism=random.randint(1, 5)
            )
            db.session.add(new_profile)

            # Create user preferences
            new_preferences = UserPreferences(
                user=new_user,
                activity_historical=fake.boolean(),
                activity_outdoor=fake.boolean(),
                activity_beach=fake.boolean(),
                activity_cuisine=fake.boolean(),
                activity_cultural=fake.boolean()
            )
            db.session.add(new_preferences)
        # Commit all changes to the database

        db.session.commit()

if __name__ == '__main__':
    create_fake_data()
