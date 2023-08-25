# módulos python
from datetime import datetime as dt

# módulos locais
from .main import Database
# from model.util.tools import Jsons

# class ODatabase(Jsons):
class ODatabase:
    def __init__(self, **kwargs):
        super().__init__()
        
        self.db = Database()
        self.values = {}

        if kwargs != {}:
            self.setValues(**kwargs)
            self.setValues(**self.getDatabaseValues())

    #-------------------------------------------------------------------------------------
    # métodos set
    def setTable(self, table) -> None:  
        self.table = table
        self.db.set_table(self.table)


    def setValues(self, db_values=False, **kwargs):
        """ definindo valores, `db_values` para atualizar no banco de dados os novos dados """
        for __name, __value in kwargs.items():
            self.values[__name] = __value


    def setDatabaseValues(self, **kwargs) -> None:
        """ atualizando valores no banco de dados e localmente """
        self.db.connect()

        for __name, __value in kwargs.items():
            self.db.update(column=__name, column_value=__value, condition='id', condition_value=self.db_id)

        self.getDatabaseValues()
        self.db.close()

    #-------------------------------------------------------------------------------------
    # métodos get
    def getDatabaseValues(self) -> dict:
        """ atualizando valores localmente """
        self.db.connect()
        self.db.set_table(self.json_pedidos[self.category]['db_table'])
        
        columns = self.json_pedidos[self.category]['columns']
        values = {}

        for column in columns:
            values[column] = self.db.read(column=column, where='id', value=self.db_id)[0][0]

        # processo, status = self.db.command(F'SELECT processo, status FROM db_certfy.status_pedidos where id_category = "{self.db_id_category}"', 'fetchall')[0]
        
        # self.db.set_table("var")
        # if self.db_id_category in self.db.read_column("id_category"):
        #     horario = self.db.read(column="horario", where="id_category", value=self.db_id_category)[0][0]
        
        # else:
        #     horario = "00:00"

        # horario = self.db.read(column="horario", where="id_category", value=self.db_id_category)[0][0]
        # num_pedido = self.db.read(column="num_pedido", where="id_category", value=self.db_id_category)[0][0]
        # codigo_instalacao = self.db.read(column="codigo_instalacao", where="id_category", value=self.db_id_category)[0][0]

        # self.setValues(processo=processo, status=status, horario=horario, num_pedido=num_pedido, codigo_instalacao=codigo_instalacao, **values)
        self.setValues(**values)
        self.db.close()

        return values
    

    def getEtapa(self, status):
        """ retorna id_solicitacao, category """
        self.db.connect()
        values = self.db.command(f'SELECT id_solicitacao, category from status_pedidos where status = "{status.upper()}"', command_type='fetchall')
        self.db.close()

        return values
    #-------------------------------------------------------------------------------------