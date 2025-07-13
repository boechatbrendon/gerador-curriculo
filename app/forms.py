from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, TextAreaField, SubmitField, TelField, FieldList, FormField, PasswordField

from wtforms.validators import DataRequired, Email


# Subformulario de endereco
class EnderecoForm(FlaskForm):
    cep = StringField('CEP', validators=[DataRequired()])
    logradouro = StringField('Logradouro', validators=[DataRequired()])
    numero = StringField('Número', validators=[DataRequired()])
    complemento = StringField('Complemento')
    bairro = StringField('Bairro', validators=[DataRequired()])
    municipio = StringField('Município', validators=[DataRequired()])
    uf = SelectField('UF', choices=[
        ('SP', 'SP'), ('RJ', 'RJ'), ('MG', 'MG')
    ], validators=[DataRequired()])


# Subformulario de experiencia profisional
class ExperienciaProfissionalForm(FlaskForm):
    cargo = StringField('Cargo', validators=[DataRequired()])
    empresa = StringField('Empresa', validators=[DataRequired()])
    descricao = TextAreaField('Descrição das atividades', validators=[DataRequired()])
    data_inicio = DateField('Data de Início', validators=[DataRequired()])
    data_fim = DateField('Data de Término (ou atual)', validators=[DataRequired()])


# Subformulario de formacao academica
class FormacaoAcademicaForm(FlaskForm):
    nome_formacao = StringField('Nome da Formação', validators=[DataRequired()])
    instituicao = StringField('Instituição de Ensino', validators=[DataRequired()])
    nivel = SelectField('Nível', choices=[
        ('fundamental', 'Ensino Fundamental'),
        ('medio', 'Ensino Médio'),
        ('tecnico', 'Técnico'),
        ('superior', 'Superior'),
        ('pos', 'Pós-graduação'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
        ('outro', 'Outro')
    ], validators=[DataRequired()])
    situacao = SelectField('Situação', choices=[
        ('concluido', 'Concluído'),
        ('andamento', 'Em andamento'),
        ('incompleto', 'Incompleto')
    ], validators=[DataRequired()])
    data_inicio = DateField('Data de Início', validators=[DataRequired()])
    data_conclusao = DateField('Data de Conclusão (ou prevista)')
    carga_horaria = StringField('Carga Horária')


# Subformulario de abilidades
class HabilidadeForm(FlaskForm):
    habilidade = StringField('Habilidade', validators=[DataRequired()])
    nivel_conhecimento = SelectField('Nível de Conhecimento', choices=[
        ('basico', 'Básico'),
        ('intermediario', 'Intermediário'),
        ('avancado', 'Avançado'),
        ('domina', 'Domina')
    ], validators=[DataRequired()])


# Subformulario de cursos
class CursoForm(FlaskForm):
    nome_curso = StringField('Nome do Curso', validators=[DataRequired()])
    instituicao = StringField('Instituição de Ensino', validators=[DataRequired()])
    situacao = SelectField('Situação', choices=[
        ('concluido', 'Concluído'),
        ('andamento', 'Em andamento'),
        ('incompleto', 'Incompleto')
    ], validators=[DataRequired()])
    carga_horaria = StringField('Carga Horária')


# Formulario Principal
class FormDado(FlaskForm):
    # Dados Pessoais
    nome = StringField('Nome completo', validators=[DataRequired()])
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()])
    sexo = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    estado_civil = SelectField('Estado Civil', choices=[
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)')
    ])
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    telefone = TelField('Telefone', validators=[DataRequired()])
    whatsapp = TelField('WhatsApp', validators=[DataRequired()])
    
    cargo = StringField('Cargo desejado', validators=[DataRequired()])
    sobre_min = TextAreaField('Sobre mim', validators=[DataRequired()])

    # Botao
    btn_GerarCurriculo = SubmitField('Gerar Currículo')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btn_login = SubmitField('Logar')
