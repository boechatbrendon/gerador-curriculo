from app import db

# --------------------
# Tabela principal: Curriculo
# --------------------
class Curriculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.String(20), nullable=False)
    sexo = db.Column(db.String(10))
    estado_civil = db.Column(db.String(20))
    email = db.Column(db.String(120), nullable=False)
    
    telefone = db.Column(db.String(20))
    whatsapp = db.Column(db.String(20))
    cargo = db.Column(db.String(100))
    sobre_min = db.Column(db.Text)
    informacoes_adicionais = db.Column(db.Text)

    endereco = db.relationship('Endereco', backref='curriculo', uselist=False)
    experiencias = db.relationship('ExperienciaProfissional', backref='curriculo', cascade="all, delete-orphan")
    formacoes = db.relationship('FormacaoAcademica', backref='curriculo', cascade="all, delete-orphan")
    cursos = db.relationship('Curso', backref='curriculo', cascade="all, delete-orphan")
    habilidades = db.relationship('Habilidade', backref='curriculo', cascade="all, delete-orphan")


# --------------------
# Endereco (One-to-One)
# --------------------
class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(20))
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(10))
    complemento = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    municipio = db.Column(db.String(100))
    uf = db.Column(db.String(2))
    curriculo_id = db.Column(db.Integer, db.ForeignKey('curriculo.id'))


# --------------------
# Experiencia Profissional (One-to-Many)
# --------------------
class ExperienciaProfissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(100))
    empresa = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    data_inicio = db.Column(db.String(20))
    data_fim = db.Column(db.String(20))
    curriculo_id = db.Column(db.Integer, db.ForeignKey('curriculo.id'))


# --------------------
# Formnacao Academica (One-to-Many)
# --------------------
class FormacaoAcademica(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_formacao = db.Column(db.String(100))
    instituicao = db.Column(db.String(100))
    nivel = db.Column(db.String(50))
    situacao = db.Column(db.String(50))
    data_inicio = db.Column(db.String(20))
    data_conclusao = db.Column(db.String(20))
    carga_horaria = db.Column(db.String(20))
    curriculo_id = db.Column(db.Integer, db.ForeignKey('curriculo.id'))


# --------------------
# Curso (One-to-Many)
# --------------------
class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(100))
    instituicao = db.Column(db.String(100))
    situacao = db.Column(db.String(50))
    carga_horaria = db.Column(db.String(20))
    curriculo_id = db.Column(db.Integer, db.ForeignKey('curriculo.id'))


# --------------------
# Habilidade (One-to-Many)
# --------------------
class Habilidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habilidade = db.Column(db.String(100))
    nivel_conhecimento = db.Column(db.String(50))
    curriculo_id = db.Column(db.Integer, db.ForeignKey('curriculo.id'))