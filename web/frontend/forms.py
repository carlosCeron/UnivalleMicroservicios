from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ProfesorForm(FlaskForm):
    primerNombre = StringField('Primer Nombre', validators=[DataRequired()])
    segundoNombre = StringField('Segundo Nombre', validators=[DataRequired()])
    primerApellido = StringField('Primer Apellido', validators=[DataRequired()])
    segundoApellido = StringField('Segundo Apellido', validators=[DataRequired()])
    profesion = StringField('Profesion', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    submit = SubmitField('Crear')


class EstudianteForm(FlaskForm):
    nombreEstudiante = StringField('Nombre Estudiante', validators=[DataRequired()])
    direccion = StringField('Direccion', validators=[DataRequired()])
    telefono = StringField('Telefono', validators=[DataRequired()])
    identificacion = StringField('Identificacion', validators=[DataRequired()])
    sede = StringField('Sede', validators=[DataRequired()])
    submit = SubmitField('Crear Estudiante')


class CursoForm(FlaskForm):
    nombreCurso = StringField('Nombre Curso', validators=[DataRequired()])
    descripcion = StringField('Descripcion', validators=[DataRequired()])
    horas = StringField('Horas', validators=[DataRequired()])
    sede = StringField('Sede', validators=[DataRequired()])
    submit = SubmitField('Crear Curso')