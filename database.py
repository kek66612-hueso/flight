import psycopg2

class DatabaseConfig:
    '''Класс конфигурации БД'''
    def __init__(self,
                 database: str = "", 
                 host: str="", 
                 user:str = "", 
                 password:str = "",
                 port:str=""):
        self.host=host,
        self.database=database,
        self.user=user,
        self.password=password,
        self.port=port

    def get_connection_params(self):
        return{
            'host':self.host,
            'database':self.database,
            'user':self.user,
            'password':self.password,
            'port':self.port
        }
    
class DatabaseConnection:
    '''Класс подключения к БД'''

    def __init__(self, config:DatabaseConfig):
        self.config = config
        self._connection = None
    
    def get_connection(self):
        if self._connection is None or self._connection.closed:
            self._connection = psycopg2.connect(**self.config.get_connection_params())
        return self._connection

    def close_connection(self):
        if self._connection and not self._connection.closed:
            self._connection.close()