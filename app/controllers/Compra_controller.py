from app import app
from app.dao.Compra_dao import Compra_dao
from app.service.Compra_service import Compra_service
from flask import jsonify


@app.route("/compra")
def salvar_compra():
    i = Compra_dao(3, 2.5, '23/11/2017', 1)
    service = Compra_service()
    return jsonify(service.salvar(i))

@app.route("/compra/list")
def lista_todos_compra():
    service = Compra_service()
    service.findAll()
    return jsonify(service.findAll())

