from app.dao.Produto_dao import Produto_dao


class Produto_service(object):

    def salvar(self, produto):
        p = self.filter_nome(produto.nome)
        if p == None:
            produto.salvar()
            return {'mensagem':'Produto cadastrado com sucesso'}
        else:
            return {'mensagem':'Nome de produto ja cadastrado'}

    def update(self, produto):
        print(produto.quantidade)
        Produto_dao.update(produto)

    def listar(self, id):
        return Produto_dao.listar(id)

    @staticmethod
    def findAll():
        produtos = []
        for produto in Produto_dao.findAll():
            print(produto.to_JSON())
            produtos.append(produto.to_JSON())
        return produtos

    @staticmethod
    def findById(id_produto):
        return Produto_dao.findById(id_produto)

    @staticmethod
    def filter_nome(nome):
        return Produto_dao.filter_nome(nome)