from seeds.seed_db import *

# call the seed_test_data function
def setup_test_data():
    seed_test_data()

# call the create_tables function
def setup_tables():
    create_db_tables()

# setup tables if ran directly
if __name__ == "__main__":
    setup_tables()