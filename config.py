import os

SECRET_KEY = 'alohomora'

SQLALCHEMY_DATABASE_URI = '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'admin',
    servidor = 'localhost',
    database = 'gamelibrary'
)

UPLOAD_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')