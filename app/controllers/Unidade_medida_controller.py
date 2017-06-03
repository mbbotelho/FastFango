from app import app
from app.dao.Unidade_medida_dao import Unidade_medida_dao
from app.service.Unidade_medida_service import Unidade_medida_service
from flask import jsonify
import json

service = Unidade_medida_service()

@app.route("/unidadeMedida")
def salva_unidade_medida():
    unidade = Unidade_medida_dao("M")
    return jsonify(service.salvar(unidade))

@app.route("/unidadeMedida/list")
def findAll_unidade():
    return jsonify(service.findAll())


@app.route("/unidadeMedida/<id>")
def findById_unidade(id):
    service.findById(id)
    return 'ok'
