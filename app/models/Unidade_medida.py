import json
class Unidade_medida():
    id_unidade_medida = None
    nome = None

    def __init__(self, nome):
        self.nome = nome

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
