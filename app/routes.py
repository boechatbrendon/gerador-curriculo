from app import app, db
from flask import render_template, redirect, url_for
from app.forms import FormDado
from app.models import Curriculo

@app.route('/', methods=['GET', 'POST'])
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
        )
        db.session.add(curriculo)
        db.session.commit()
    return render_template('curriculo_form.html', form=form)