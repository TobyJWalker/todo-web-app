import peewee, os
from datetime import datetime

APP_ENV = os,os.environ.get("APP_ENV")

if APP_ENV == "test":
    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    DB_HOST = 'localhost'
    DB_PORT = 5432

    db = peewee.PostgresqlDatabase(
        DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

else:
    db = peewee.PostgresqlDatabase('todo-db')


class User(peewee.Model):
    username = peewee.CharField(unique=True)
    password = peewee.CharField()
    email = peewee.CharField(unique=True)

    class Meta:
        database = db