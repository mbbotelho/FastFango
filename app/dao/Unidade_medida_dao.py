from app import db
from app.models.Unidade_medida import Unidade_medida
from sqlalchemy.orm import relationship


class Unidade_medida_dao(db.Model):
    __tablename__ = "unidademedida"
    id_unidade_medida = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    produto = relationship("Produto_dao", back_populates="unidade", uselist=False)



    def __init__(self, nome):
        self.nome = nome

    def salvar(self):
        print(self.nome)
        db.session.add(self)
        db.session.commit()

    def to_JSON(self):
        unidade= Unidade_medida(self.nome)
        return unidade.to_JSON()

    @staticmethod
    def listar(id):
        print(Unidade_medida_dao.query.get(id).to_JSON)
        return Unidade_medida_dao.query.get(id)

    @staticmethod
    def findAll():
        return Unidade_medida_dao.query.all()

    @staticmethod
    def findById(id_produto):
        return Unidade_medida_dao.query.get(id_produto)

    @staticmethod
    def filter_nome(nome):
        return Unidade_medida_dao.query.filter_by(nome=nome).first()




