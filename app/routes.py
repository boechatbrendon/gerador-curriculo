from app import app
from flask import render_template
from app.forms import FormDado

@app.route('/')
def home():
    form = FormDado()
    return render_template('index.html', form=form)