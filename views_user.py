from flask import render_template, request, redirect, session, flash, url_for
from gamelibrary import app, db
from models import  Usuarios
from helpers import usuario_logado, FormularioLogin, FormularioCadastro
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima is None:
        proxima = url_for("index")
    form = FormularioLogin()
    return render_template('login.html', proxima=proxima, titulo="Faça seu Login", form=form, usuario_logado=usuario_logado())

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioLogin(request.form)
    
    if form.validate_on_submit():
        nickname = form.nickname.data
        usuario = Usuarios.query.filter_by(nickname=nickname).first()
        if usuario:
            senha = check_password_hash(usuario.senha, form.senha.data)
            if senha:
                session['usuario_logado'] = usuario.nickname
                flash(usuario.nickname + ' logado com sucesso!')
                proxima_pagina = request.form['proxima']
                return redirect(proxima_pagina)
            else:
                flash('Senha incorreta...')
        else:
            flash('Usuário não encontrado...')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    proxima = request.args.get('proxima')
    if proxima:
        return redirect(url_for(proxima))
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/cadastro')
def cadastro():
    if usuario_logado():
        return redirect('logout', proxima=url_for('cadastro'))
    form = FormularioCadastro()
    return render_template('cadastro.html', titulo="Cadastro", form=form, usuario_logado=usuario_logado())
    

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    form = FormularioCadastro(request.form)
    
    if form.validate_on_submit():
        nickname = form.nickname.data
        nome = form.nome.data
        senha = generate_password_hash(form.senha.data).decode('utf-8')
        
        usuario_existente = Usuarios.query.filter_by(nickname=nickname).first()
        
        if usuario_existente:
            flash('Usuário já cadastrado...')
            return redirect(url_for('login'))
        
        novo_usuario = Usuarios(nickname=nickname, nome=nome, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        flash('Usuário cadastrado com sucesso!')
        return redirect(url_for('login'))
    flash('Dados inválidos...')