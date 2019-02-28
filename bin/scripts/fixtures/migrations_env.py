"""migrations env.py file as fixture representation."""

env = """from __future__ import with_statement
from os import environ
from alembic import context
from app.{0}.blueprints.{0} import models
from sqlalchemy import create_engine, pool
from logging.config import fileConfig
#from nubi.bank.db import Base <- CHANGE TO THE REAL DB SETTING DIRECTORY


config = context.config
fileConfig(config.config_file_name)
target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    conn_string = config.get_main_option("test_database")
    if conn_string is None:
        conn_string = environ.get("DB_CONN_STRING")

    connectable = create_engine(conn_string)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()"""