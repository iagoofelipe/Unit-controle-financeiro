""" 
classe reservada para requisições ao servidor (banco de dados, http requests).
Construído para ser utilizado como requisições GET | POST
"""

from ._Database import Database
from ._Requests import Requests
import logging

class Server:
    def __init__(self):
        logging.debug("Server iniciando conexão database")
        self.db = Database()
        logging.debug(f"Server database connection: {self.db.test_connection()}")

        logging.debug("Server requisições (Requests)")
        self.requests = Requests()

    def checkUserPassword(self, user, password):
        """ verifica se o usuário e senha são válidos """
        self.db.set_table("users")
        results = self.db.read(where='user', value='user')
        
        if len(results) == 0:
            return False
        
        for ide, _user, _password in results:
            if password == _password:
                return True
        return False