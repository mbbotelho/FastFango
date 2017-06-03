from app import db
from app.models.Compra import Compra
from sqlalchemy.orm import relationship


class Compra_dao(db.Model):
    __tablename__ = "compra"
    id_compra = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)
    data = db.Column(db.String)
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'))
    produto = relationship("Produto_dao", back_populates="compra")

    def __init__(self, quantidade, valor, data, id_produto):
        self.quantidade = quantidade
        self.valor = valor
        self.data = data
        self.id_produto = id_produto

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