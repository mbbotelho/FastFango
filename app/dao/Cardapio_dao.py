from app import db
from app.models.Compra import Compra
from sqlalchemy.orm import relationship


class Cardapio_dao(db.Model):
    __tablename__ = "cardapio"
    id_cardapio = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Integer)
    valor = db.Column(db.Float)


    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


    def to_JSON(self):
        p = Compra(self.id_compra, self.quantidade, self.valor, self.produto.nome)
        print(p.id_compra, self.produto.nome)
        return p.to_JSON()

    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def listar(id):
        return Compra_dao.query.get(id)

    @staticmethod
    def findAll():
        return Compra_dao.query.all()