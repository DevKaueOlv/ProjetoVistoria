from pyorient import OrientDB
import os

class OrientDBConnection:
    def __init__(self):
        self.client = OrientDB(os.getenv("ORIENTDB_HOST"), int(os.getenv("ORIENTDB_PORT")))
        self.session_id = None
        self.database = os.getenv("ORIENTDB_DATABASE")
        self.username = os.getenv("ORIENTDB_USERNAME")
        self.password = os.getenv("ORIENTDB_PASSWORD")

    def connect(self):
        self.session_id = self.client.connect(self.username, self.password)
        if self.client.db_exists(self.database):
            self.client.db_open(self.database, self.username, self.password)
        else:
            print("Database does not exist.")

    def close(self):
        self.client.db_close()
