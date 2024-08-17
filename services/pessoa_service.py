import hashlib
from pymongo import MongoClient

client = MongoClient('mongodb://mongodb:27017/')
db = client.pessoa_db
collection = db.pessoas

def gera_token_md5(nome_pessoa):
    return hashlib.md5(nome_pessoa.encode()).hexdigest()

def cadastra_pessoa(id, nome_pessoa):
    token = gera_token_md5(nome_pessoa)
    pessoa = {"id": id, "nome_pessoa": nome_pessoa, "token": token}
    collection.insert_one(pessoa)
    return pessoa

def lista_pessoas():
    return list(collection.find({}, {"_id": 0}))
