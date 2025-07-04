import pymysql

DB_HOST = '127.0.0.1'
BD_USER = 'EngSoftII'
BD_PASSWORD = 'trabalhoLucao'
BD_NAME = 'agenda'

class DatabaseConnection:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._connection = pymysql.connect(
                host=DB_HOST,
                user=BD_USER,
                password=BD_PASSWORD,
                db=BD_NAME
            )
        return cls._instance

    def get_connection(self):
        return self._connection
