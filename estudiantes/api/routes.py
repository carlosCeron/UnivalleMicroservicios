from flask import jsonify, json, request, make_response
from . import estudiantes_api
from models import db, Estudiante


# Obtener Cursos

@estudiantes_api.route("/api/v1/estudiantes", methods=['GET'])
def list():
    data = []
    for row in Estudiante.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response


@estudiantes_api.route("/api/v1/estudiantes", methods=["POST"])
def create():
    nombre_estudiante = request.json['nombre_estudiante']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    identificacion = request.json['identificacion']
    sede = request.json['sede']

    estudiante = Estudiante()
    estudiante.nombre_estudiante = nombre_estudiante
    estudiante.direccion = direccion
    estudiante.telefono = telefono
    estudiante.identificacion = identificacion
    estudiante.sede = sede
    db.session.add(estudiante)
    db.session.commit()

    return jsonify({'msg': estudiante.to_json(), 'status': 'Estudiante creado correctamente'})


@estudiantes_api.route("/api/v1/estudiantes/<id>", methods=["GET"])
def edit(id):
    estudiante = Estudiante.query.filter_by(id=id).first()
    if estudiante is not None:
        response = jsonify({'Estudiante': estudiante.to_json()})
    else:
        response = jsonify({'mensaje': 'Estudiante no existe'})

    return response


@estudiantes_api.route("/api/v1/estudiantes/<id>", methods=["PUT"])
def update(id):
    estudiante = Estudiante.query.filter_by(id=id).first()
    if estudiante is not None:
        # Obtenemos los datos que se van a actualizar

        nombre_estudiante = request.json['nombre_estudiante']
        direccion = request.json['direccion']
        telefono = request.json['telefono']
        identificacion = request.json['identificacion']
        sede = request.json['sede']

        # Actualizamos los datos

        estudiante.nombre_estudiante = nombre_estudiante
        estudiante.direccion = direccion
        estudiante.telefono = telefono
        estudiante.identificacion = identificacion
        estudiante.sede = sede
        db.session.commit()

        response = jsonify({'Estudiante': estudiante.to_json()})
    else:
        response = jsonify({'mensaje': 'Estudiante no existe'})

    return response


@estudiantes_api.route("/api/v1/estudiantes/<id>", methods=["DELETE"])
def delete(id):
    estudiante = Estudiante.query.filter_by(id=id).first()
    if estudiante is not None:
        db.session.delete(estudiante)
        db.session.commit()
        return jsonify({'msg': 'Estudiante con el ID ' + id + ' fue eliminado', 'registro': estudiante.to_json()})
    else:
        return jsonify({'msg': 'Estudiante no encontrado'})


