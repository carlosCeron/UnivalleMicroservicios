from flask import render_template, request, redirect, url_for
import requests
from . import frontend_blueprint
from . import forms
from .api.ProfesorCliente import ProfesorCliente
from .api.EstudianteCliente import EstudianteCliente
from .api.CursosCliente import CursosCliente
import random


@frontend_blueprint.route('/', methods=['GET'])
def home():
    return render_template('home/index.html')


@frontend_blueprint.route('/profesores', methods=['GET'])
def profesores():

    try:
        profesores = ProfesorCliente.get_profesores()
    except requests.exceptions.ConnectionError:
        profesores = []
    return render_template('profesores/index.html', profesores=profesores)

@frontend_blueprint.route('/profesores/new', methods=['GET', 'POST'])
def new_proferor():
    form = forms.ProfesorForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            profesor = ProfesorCliente.post_profesor_create(form)
            if profesor:
                return redirect(url_for('frontend.profesores'))

    return render_template('profesores/nuevo.html', form=form)



@frontend_blueprint.route('/estudiantes', methods=['GET'])
def estudiantes():
    try:
        estudiantes = EstudianteCliente.get_estudiantes()
    except requests.exceptions.ConnectionError:
        estudiantes = []
    return render_template('estudiantes/index.html', estudiantes=estudiantes)


@frontend_blueprint.route('/estudiantes/new', methods=['GET', 'POST'])
def new_estudiante():
    form = forms.EstudianteForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            estudiante = EstudianteCliente.post_estudiante_create(form)
            if estudiante:
                return redirect(url_for('frontend.estudiantes'))

    return render_template('estudiantes/nuevo.html', form=form)


@frontend_blueprint.route('/cursos', methods=['GET'])
def cursos():
    try:
        cursos = CursosCliente.get_cursos()
    except requests.exceptions.ConnectionError:
        cursos = []

    return render_template('cursos/index.html', cursos=cursos)


@frontend_blueprint.route('/cursos/new', methods=['GET', 'POST'])
def new_curso():
    form = forms.CursoForm(request.form)

    if request.method == "POST":
        if form.validate_on_submit():
            curso = CursosCliente.post_curso_create(form)
            if curso:
                return redirect(url_for('frontend.cursos'))

    return render_template('cursos/nuevo.html', form=form)
