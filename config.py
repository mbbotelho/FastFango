import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'teste2.db')
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:ifes@localhost:5432/teste'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '123456'