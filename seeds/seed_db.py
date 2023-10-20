from lib.models import *

# force reset tables to empty state
def _reset_tables():
    db.drop_tables([User])
    db.create_tables([User])

# create empty tables if they don't exist
def create_db_tables():
    db.create_tables([User])

# seed the database with test data
def seed_test_data():
    _reset_tables()

    # create test users
    User.create(
        username="test_1", 
        password="test_1_password", 
        email="test_1@example.com"
        )
    User.create(
        username="test_2", 
        password="test_2_password", 
        email="test_2@example.com"
    )
    User.create(
        username="test_3",
        password="test_3_password",
        email="test_3@example.com"
    )
