from app.dao.Compra_dao import Compra_dao
from app.dao.Produto_dao import Produto_dao


class Compra_service(object):
    def salvar(self, compra):
        produto = Produto_dao.findById(compra.id_produto)
        if produto != None:
            produto.quantidade += compra.quantidade
            compra.salvar()
            return {'mensagem': 'Compra cadastrado com sucesso'}
        else:
            return {'mensagem': 'Produto da compra nao existe'}
        
    def listar(self, id):
        return Compra_dao.listar(id)

    @staticmethod
    def findAll():
        compras = []
        print('findAll', Compra_dao.findAll())
        for compra in Compra_dao.findAll():
            print(compra.to_JSON())
            compras.append(compra.to_JSON())
        return compras

