""" 
classe reservada para requisições ao servidor (banco de dados, http requests).
Construído para ser utilizado como requisições GET | POST
"""

from ._Database import Database
from ._Requests import Requests
from ._Crypto import Crypto
import logging, configparser, os

class Server:
    def __init__(self):
        logging.debug("Server iniciando conexão database")
    #     self.db = Database()
    #     db_connection = self.db.test_connection()
    #     logging.debug(f"Server database connection: {db_connection}")
    #     if not db_connection:
    #         raise ConnectionError("Não foi possível estabelecer a conexão com o banco de dados")

    #     logging.debug("Server requisições (Requests)")
    #     self.requests = Requests()
    #     self.crypto = Crypto(self.requests.defaults["key"])

    # def checkUserPassword(self, user, password):
    #     """ verifica se o usuário e senha são válidos """
        
    #     self.db.set_table("users")
    #     results = self.db.read()
        
    #     if len(results) == 0:
    #         return False
        
    #     for ide, _user, _password in results:
    #         _user = self.crypto.decode(_user)
    #         _password = self.crypto.decode(_password)
    #         if _user == user and _password == password:
    #             return True
    #     return False
    
    # def createUser(self, user, password):
    #     self.db.set_table("users")
    #     user = self.crypto.encode(user, "str")
    #     password = self.crypto.encode(password, "str")
    #     self.db.create(user=user, password=password)
        
    
    # @staticmethod
    # def setCfgFile(file: str, **kwargs) -> None:
    #     if 'cfg' in kwargs:
    #         config = kwargs['cfg']

    #     else:        
    #         if not os.path.exists(file):
    #             with open(file, 'w') as f:
    #                 f.write('')

    #         config = __class__.getCfgFile(file)
    #         for key, value in kwargs.items():
    #             config[key] = value

    #     with open(file, 'w') as cfg:
    #         config.write(cfg)        

    # @staticmethod
    # def getCfgFile(fileName) -> configparser.ConfigParser:
    #     config = configparser.ConfigParser()
    #     config.read(fileName)
    #     return config