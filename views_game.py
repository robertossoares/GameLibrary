from flask import render_template, request, redirect, flash, url_for, send_from_directory
from gamelibrary import app, db
from models import Jogos
from os import path
from helpers import usuario_logado, recupera_imagem, deleta_imagem, FormularioJogo
from time import time

@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', usuario_logado=usuario_logado(), jogos=lista)

@app.route('/novo')
def novo():
    if not usuario_logado():
        return redirect(url_for('login', proxima=url_for('novo')))
    form = FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo', form=form, usuario_logado=usuario_logado())

@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioJogo(request.form)
    
    if not form.validate_on_submit():
        flash('Formulário inválido')
        return redirect(url_for('novo'))
    
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data
    jogo = Jogos.query.filter_by(nome=nome).first()
    if jogo:
        flash('Jogo já existente!')
    else:
        novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
        db.session.add(novo_jogo)
        db.session.commit()
        
        imagem = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        
        imagem.save(path.join(upload_path, f'{int(time())}_capa_{novo_jogo.id}.jpg'))
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    jogo = Jogos.query.filter_by(id=id).first()
    if not usuario_logado():
        return redirect(url_for('login', proxima=url_for('editar', id=jogo.id)))
    capa_jogo = recupera_imagem(id)
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    return render_template('editar.html', titulo='Editando Jogo', id=jogo.id, form=form, capa_jogo=capa_jogo, usuario_logado=usuario_logado())

@app.route('/atualizar', methods=['POST'])
def atualizar():
    form = FormularioJogo(request.form)
    
    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = request.form['nome']
        jogo.categoria = request.form['categoria']
        jogo.console = request.form['console']   
        db.session.add(jogo)
        db.session.commit()
        imagem = request.files['arquivo']
        upload_path = app.config['UPLOAD_PATH']
        deleta_imagem(id=jogo.id)
        imagem.save(path.join(upload_path, f'{int(time())}_capa_{jogo.id}.jpg'))
   
    return redirect(url_for('index'))
   
@app.route('/deletar/<int:id>')
def deletar(id):
    if not usuario_logado():
        return redirect(url_for('login'))
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
