import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv()


class Database(object):

    def __init__(self):
        try:
            connect = psycopg2.connect("dbname='" + os.getenv("POSTGRES_DB") + "' user='" + os.getenv("POSTGRES_USER") +
                                       "' host='" + os.getenv("POSTGRES_HOST") + "' password='" + os.getenv("POSTGRES_PASSWORD") +
                                       "' port='" + os.getenv("POSTGRES_PORT") + "'")
            connect.autocommit = True
            self.__connect = connect
            self.__query = connect.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            self.__connect = None
            self.__query = None
            print(error)

    @property
    def connect(self):
        return self.__connect

    @property
    def query(self):
        return self.__query

