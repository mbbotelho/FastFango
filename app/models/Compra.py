import json

class Compra():
    id_compra = None
    quantidade = None
    valor = None
    data = None
    produto = None

    def __init__(self, id_compra, quantidade, valor, produto):
        self.id_compra = id_compra
        self.quantidade = quantidade
        self.valor = valor
        #self.data = dataz
        self.produto = produto

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
