import json

class prod():
    nome = None
    quantidade = None

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)