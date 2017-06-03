from app.dao.Unidade_medida_dao import Unidade_medida_dao


class Unidade_medida_service(object):
    def salvar(self, unidade):
        u = self.filter_nome(unidade.nome)
        if u == None:
            unidade.salvar()
            return {'mensagem': 'Unidade cadastrado com sucesso'}
        else:
            return {'mensagem': 'Nome de Unidade ja cadastrado'}

    def update(self, produto):
        print(produto.quantidade)
        Unidade_medida_dao.update(produto)

    def listar(self, id):
        return Unidade_medida_dao.listar(id)

    @staticmethod
    def findAll():
        unidade_medidas = {}
        for unidade_medida in Unidade_medida_dao.findAll():
            print(unidade_medida.to_JSON())
            unidade_medidas[unidade_medida.id_unidade_medida] = unidade_medida.to_JSON()
        print(unidade_medidas)
        return unidade_medidas

    @staticmethod
    def filter_nome(nome):
        return Unidade_medida_dao.filter_nome(nome)
