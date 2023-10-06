# módulos python
from PySide6.QtCore import QObject, QTimer, Signal
import logging

# módulos locais

class ModelLogin(QObject):

    def __init__(self, view):
        super().__init__()
        self._users = dict # set by controller
        
        # atributos gerais
        self._view = view
        self._main_model = view._main_model

        # atributos privados
        self._timer = QTimer()

        # métodos gerais
        # métodos privados
        self._user:str = self._main_model.crypto.decode(self._main_model.cfg_default['LOGIN']['user'])
        self._password:str = self._main_model.crypto.decode(self._main_model.cfg_default['LOGIN']['password'])
        self._remember:bool = self._main_model.cfg_default['LOGIN']['remember'] == "True"
    
    #-------------------------------------
    # property
    @property
    def users(self):
        return self._users
    
    @users.setter
    def users(self, db_values):
        """ definindo valores de usuário e senha """
        self._users = {}

        for ide, user, password, username in db_values:
            user = self._main_model.crypto.decode(user)
            password = self._main_model.crypto.decode(password)
            self._users[user] = {"password":password, "username": username}

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self, value):
        self._user = value
        user_encode = self._main_model.crypto.encode(value, "str")
        self._main_model.cfg_default = dict(LOGIN={"user":user_encode})
        
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value
        password_encode = self._main_model.crypto.encode(value, "str")
        self._main_model.cfg_default = dict(LOGIN={"password":password_encode})
    
    @property
    def remember(self):
        return self._remember
    @remember.setter
    def remember(self, value):
        self._remember = value
        self._main_model.cfg_default = dict(LOGIN={"remember":str(value)})
    #-------------------------------------
    # Signal
    #-------------------------------------