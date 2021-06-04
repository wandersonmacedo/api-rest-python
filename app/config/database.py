import psycopg2
import os
from dotenv import load_dotenv, find_dotenv


class Database:

    def __init__(self):
        try:

            self.conection = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                database=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD")
            )
            self.cursor = self.conection.cursor()
        except:

            print("ERROR TRYING TO CONNECT THE DATABASE")
