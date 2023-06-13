from pydantic import BaseModel

class Produto(BaseModel):
    categoria: str
    nome: str
    descricao: str
    preco: float
