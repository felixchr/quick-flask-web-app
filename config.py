import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/felixc.db')
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@127.0.0.1:43306/felixc'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
