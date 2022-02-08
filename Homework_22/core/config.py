from .singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.driver_name = "postgresql+psycopg2"
        self.database = "store"
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = "ihorpostgres"
