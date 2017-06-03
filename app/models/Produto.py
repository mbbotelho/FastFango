import json

class Produto():
    id_produto = None
    nome = None
    quantidade = None
    unidade_medida = None
    quantidade = None
    qtd_minima = None
    item_estoque_vld = None

    def __init__(self, id_produto, nome, quantidade, unidade_medida, qtd_minima, item_estoque_vld):
        self. id_produto = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.unidade_medida = unidade_medida
        self.qtd_minima = qtd_minima
        self.item_estoque_vld = item_estoque_vld

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)