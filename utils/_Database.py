# módulos python
from mysql.connector import connect
from my_tools import File, resource_path
from typing import Literal

class Database:
    def __init__(self, table=None):
        if table != None:
            self.set_table(table)

        self.__json = File.getFile(resource_path('connect.json')) # armazenando host e banco
    #------------------------------------------------------------------------------------
    # connection
    def connect(self) -> bool:
        """ iniciando conexão com o banco definido no arquivo `connect.json` """
        try:
            self.conexao = connect(**self.__json)
            self.cursor = self.conexao.cursor()
            return True
            
        except:
            return False
    

    def close(self):
        try:
            self.conexao.close()
            self.cursor.close() 
        except:
            pass
    #------------------------------------------------------------------------------------
    # table
    def set_table(self, table):
        self.__table = table
    
    @property
    def table(self):
        return self.__table
    
    @property
    def lastRowId(self) -> int | None:
        self.connect()
        retorno = self.command(f"SELECT MAX(ID) FROM {self.__table}", "fetchall")[0][0]
        self.close()
        return retorno
    #------------------------------------------------------------------------------------
    # ceate
    def create(self, **kwargs):
        keys, values = '', ''
        
        for key, value in kwargs.items():
            keys += f'{key}, '
            values += f'{value}, ' if type(value) != str else f'"{value}", '

        else:
            keys = keys[:-2]
            values = values[:-2]
        
        command = f'INSERT INTO {self.table} ({keys}) VALUES ({values})'

        self.connect()
        self.cursor.execute(command)
        self.conexao.commit()
        self.close()
    #------------------------------------------------------------------------------------
    # read
    def read(self, column='*', where=None, value=None, order_by=None):
        """ SELECT `column` FROM `self.table` WHERE `where` = `value` ORDER BY `order_by`"""
        command = f'SELECT {column} FROM {self.table} '
        self.connect()
        if where != None:
            if type(value) == str:
                command += f'WHERE {where} = "{value}"'
            else:
                command += f'WHERE {where} = {value}'

        if order_by != None:
            command += f'ORDER BY {order_by}'

        self.cursor.execute(command)
        retonro = self.cursor.fetchall()
        self.close()
        return retonro
    
    def readLastsRowsByIdRange(self, numRange: int, arg='') -> list:
        """ este método funciona apenas com tabelas que possuem `ID AUTO_INCREMENT` """
        lastId = self.lastRowId
        command = f"SELECT * FROM {self.__table} WHERE ID > {lastId-numRange} AND ID < {lastId+1} {arg}"

        return self.command(command, "fetchall")


    def read_column(self, column):
        command = f'SELECT {column} FROM {self.table}'
        
        self.connect()
        self.cursor.execute(command)
        valores = []

        for i in self.cursor.fetchall():
            if i[0] not in valores:
                valores.append(i[0])

        self.close()
        return tuple(valores)
    
    #------------------------------------------------------------------------------------
    # update
    def update(self, column, column_value, condition, condition_value):
        """ 
        UPDATE `self.table` set `column` = `value` WHERE `condition` = `value`
        """
        command = f'update {self.table} set {column} = '

        if type(column_value) == str:
            command += f'"{column_value}"'
        else:
            command += f'{column_value}'
            
        command += f' WHERE ' + condition

        if type(condition_value) == str:
            command += f' = "{condition_value}"'
        else:
            command += f' = {condition_value}'
        
        self.cursor.execute(command)
        self.conexao.commit()   


    def setValues(self, db_id, **kwargs) -> None:
        """ atualizando valores no banco de dados """
        self.connect()

        for __name, __value in kwargs.items():
            self.db.update(column=__name, column_value=__value, condition='id', condition_value=db_id)
        
        self.close()

    #------------------------------------------------------------------------------------
    # others
    def command(self, command, command_type=Literal['commit', 'fetchall']):
        self.connect()
        self.cursor.execute(command)
        
        match command_type:
            case 'commit':
                self.conexao.commit()
            case 'fetchall':
                value = self.cursor.fetchall()
        
        self.close()
        return value


    # testing connection
    def test_connection(self) -> bool:
        self.connect()
        try:
            test = self.conexao.is_connected()
            self.close()
        
        except AttributeError:
            test = False

        return test
    #------------------------------------------------------------------------------------