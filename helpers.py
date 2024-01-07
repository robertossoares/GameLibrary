import os
from views_user import session
from gamelibrary import app
from wtforms import PasswordField, StringField, SubmitField, validators
from flask_wtf import FlaskForm

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1, max=80)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=1, max=50)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=30)])
    salvar = SubmitField('Salvar')
    
class FormularioLogin(FlaskForm):
    nickname = StringField('Nome de Usuário', [validators.DataRequired(), validators.Length(min=1, max=30)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
    
class FormularioCadastro(FlaskForm):
    nome = StringField('Nome Completo', [validators.DataRequired(), validators.Length(min=1, max=80)])
    nickname = StringField('Nome de Usuário', [validators.DataRequired(), validators.Length(min=1, max=30)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    cadastrar = SubmitField('Cadastrar')
    

def usuario_logado():
    return not('usuario_logado' not in session or session['usuario_logado'] == None)

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}.jpg' in nome_arquivo:
            return nome_arquivo
    return 'capa_padrao.jpg'

def deleta_imagem(id):
    arquivo = recupera_imagem(id)
    if arquivo != "capa_padrao.jpg":
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))