from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import flask_restful

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
errors = {
    'sqlalchemy.exc.IntegrityError': {
        'message': "A user with that username already exists.",
        'status': 409,
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': 410,
        'extra': "Any extra information you want.",
    },
}
api = flask_restful.Api(app, errors=errors)


from app.dao.Produto_dao import Produto_dao
from app.dao.Compra_dao import Compra_dao
from app.dao.Unidade_medida_dao import Unidade_medida_dao
from app.controllers import Produto_controller
from app.service import Produto_service
from app.controllers import Compra_controller
from app.controllers import Unidade_medida_controller
from app.service import Compra_service