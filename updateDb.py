from my_tools import File
from controllers.src import Database

dados = File.getFile("dados.csv")
db = Database("saidas")

db.connect()
for _, descricao, categoria, data, valor in dados:
    db.create(descricao=descricao, categoria=categoria, data=data, valor=valor)

db.close()
print(db.read())
# print(dados)