from fastapi import Query

from produto.produto_database import ProdutosDAO


class ProdutoService:
    def buscar_nome_produtos(nome: str):
        produtoDao = ProdutosDAO
        produtos = produtoDao.buscar_por_nome(nome) \
            if nome \
            else produtoDao.buscar_por_nome()
        return produtos