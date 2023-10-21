import peewee, os
from datetime import datetime

APP_ENV = os,os.environ.get("APP_ENV")

if APP_ENV == "test":
    db = peewee.PostgresqlDatabase(
        'todo-test-db', user='tester', password='testing', host='localhost', port=5432
    )

else:
    db = peewee.PostgresqlDatabase(os.environ.get('POSTGRES_DB'))

class User(peewee.Model):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([User])
    db.close()

if __name__ == "__main__":
    initialize_db()