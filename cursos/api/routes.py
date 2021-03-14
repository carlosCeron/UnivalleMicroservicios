from flask import jsonify, json, request, make_response
from . import curso_api
from models import db, Curso


# Obtener Cursos
@curso_api.route("/api/v1/curso", methods=['GET'])
def list():
    data = []
    for row in Curso.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response



@curso_api.route("/api/v1/curso", methods=["POST"])
def create():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    sede = request.json['sede']
    horas = request.json['horas']
    id_profesor = request.json['id_profesor']

    curso = Curso()
    curso.nombreCurso = nombre
    curso.descripcion = descripcion
    curso.sede = sede
    curso.horas = horas
    curso.idProfesor = id_profesor
    db.session.add(curso)
    db.session.commit()

    return jsonify({'msg': curso.to_json(), 'status': 'Curso creado correctamente'})


@curso_api.route("/api/v1/curso/<id>", methods=["GET"])
def edit(id):
    curso = Curso.query.filter_by(id=id).first()
    if curso is not None:
        response = jsonify({'profesor': curso.to_json()})
    else:
        response = jsonify({'mensaje': 'Curso no existe'})

    return response


@curso_api.route("/api/v1/curso/<id>", methods=["PUT"])
def update(id):
    curso = Curso.query.filter_by(id=id).first()
    if curso is not None:
        # Obtenemos los datos que se van a actualizar

        nombre_curso = request.json['nombre']
        descripcion = request.json['descripcion']
        horas = request.json['horas']
        sede = request.json['sede']
        id_profesor = request.json['id_profesor']

        # Actualizamos los datos

        curso.nombreCurso = nombre_curso
        curso.descripcion = descripcion
        curso.horas = horas
        curso.sede = sede
        curso.idProfesor = id_profesor
        db.session.commit()

        response = jsonify({'Curso': curso.to_json()})
    else:
        response = jsonify({'mensaje': 'Curso no existe'})

    return response


@curso_api.route("/api/v1/curso/<id>", methods=["DELETE"])
def delete(id):
    curso = Curso.query.filter_by(id=id).first()
    if curso is not None:
        db.session.delete(curso)
        db.session.commit()
        return jsonify({'msg': 'Curso con el ID ' + id + ' fue eliminado', 'registro': curso.to_json()})
    else:
        return jsonify({'msg': 'Curso no encontrado'})
