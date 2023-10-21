import peewee, os
from datetime import datetime

APP_ENV = os,os.environ.get("APP_ENV")

if APP_ENV == "test":
    DB_NAME = os.environ.get("TEST_DB_NAME")
    DB_USER = os.environ.get("TEST_DB_USER")
    DB_PASSWORD = os.environ.get("TEST_DB_PASSWORD")

    db = peewee.PostgresqlDatabase(
        DB_NAME, user=DB_USER, password=DB_PASSWORD, host='localhost', port=5432
    )

else:
    db = peewee.PostgresqlDatabase('todo-db')


class User(peewee.Model):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)

    class Meta:
        database = db