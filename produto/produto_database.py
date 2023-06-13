from pymongo import MongoClient
from produto.produto_model import Produto

mongo_uri = "mongodb://localhost:27017"  # conexão com MongoDB
database_name = "SmartShopAI"  # Nome do banco
collection_name = "produtos"  # Nome da coleção
client = MongoClient(mongo_uri)

class ProdutosDAO:
    def __init__(self):
        self.collection = client[database_name][collection_name]

    def criar_produto(self, produto:Produto):
        produto_dict = produto.dict()
        result = self.collection.insert_one(produto_dict)
        return str(result.inserted_id)

    def buscar_por_nome(self, nome:str):
        if nome:
            produtos = self.collection.find({"nome": {"$regex": f".*{nome}.*", "$options": "i"}})
        else:
            produtos = self.collection.find()
        return [Produto(**produto) for produto in produtos]

    def buscar_por_preco(self, preco):
        produtos = self.collection.find({"preco": preco})
        return [Produto(**produto) for produto in produtos]

    def buscar_por_categoria(self, categoria):
        produtos = self.collection.find({"categoria": categoria})
        return [Produto(**produto) for produto in produtos]
