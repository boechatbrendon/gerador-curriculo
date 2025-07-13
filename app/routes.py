from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import FormDado, FormLogin
from app.models import Curriculo, Usuario
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/', methods=['GET', 'POST'])
@login_required
def criar_curriculo():
    form = FormDado()
    if form.validate_on_submit():
        curriculo = Curriculo(
            nome=form.nome.data,
            data_nascimento=str(form.data_nascimento.data),
            sexo=form.sexo.data,
            estado_civil=form.estado_civil.data,
            email=form.email.data,
            telefone=form.telefone.data,
            whatsapp=form.whatsapp.data,
            cargo=form.cargo.data,
            sobre_min=form.sobre_min.data,
            usuario_id = current_user.id
        )
        db.session.add(curriculo)
        db.session.commit()
    return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and usuario.senha == form.senha.data:
            login_user(usuario)
            flash('Usuario conectado')
            return redirect(url_for('criar_curriculo'))
        else:
            flash('Usuario ou senha invalidos')
    return render_template('login.html', form=form)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('usuario deslogado com sucesso')
    return redirect(url_for('login'))