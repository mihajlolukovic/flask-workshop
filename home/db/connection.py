import configparser
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


class DBConnection:

    @staticmethod
    def get_engine():
        # Read application properties
        dir_path = os.path.dirname(os.path.realpath('application.properties'))
        file = os.path.join(dir_path, 'application.properties')
        config = configparser.ConfigParser()
        config.read(file)

        url = config.get("DB", "database_url")
        if not database_exists(url):
            create_database(url)
        engine = create_engine(url, pool_size=50, echo=False)
        return engine

    def db_connection(self):
        engine = self.get_engine()

        session = sessionmaker(bind=engine)()
        return session
