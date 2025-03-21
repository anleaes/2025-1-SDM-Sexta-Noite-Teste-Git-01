from categoria import Categoria

class Produto:
    def __init__(self, nome, descricao, data_fabricacao, e_ativo, categoria: Categoria):
        self._nome = nome
        self._descricao = descricao
        self._data_fabricacao = data_fabricacao
        self._e_ativo = e_ativo
        self._categoria = categoria

    def __str__(self):
        return f"{self._nome}: {self._descricao} | {self._categoria}"