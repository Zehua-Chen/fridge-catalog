"""
Utilities to help create url to the database
"""

import os
from sqlalchemy import create_engine
from flask import g


def _db_url() -> str:
    """
    Get the url to db from environment variables
    """

    db_host = os.environ["DB_HOST"]
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASSWORD"]

    return f"postgresql://{db_user}:{db_password}@{db_host}/proj1part2"


def init_db() -> None:
    g.engine = create_engine(_db_url())
