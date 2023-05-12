import mysql.connector as mydb
import configparser
from os import getcwd


class DB:

    def __enter__(self):
        return self
    
    # 製作者：出田(2023/3/14)----------------------

    def __init__(self):
        path = getcwd()
        config_ini = configparser.ConfigParser()
        config_ini.read(f'{path}\\config\\config.ini', encoding='utf-8')
        host = config_ini['MySQLConnection']['host']
        port = config_ini['MySQLConnection']['port']
        user = config_ini['MySQLConnection']['user']
        password = config_ini['MySQLConnection']['password']
        database = config_ini['MySQLConnection']['database']
    # コネクションの作成
        self.connect = mydb.connect(
            host = str(host),
            port = str(port),
            user = str(user),
            password= str(password),
            database= str(database)
        )
        
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.connect.close()

    def cursor_create(self):
        return self.connect.cursor(buffered=True)
