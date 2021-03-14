from flask import jsonify, json, request, make_response, logging
from . import profesores_api
from models import db, Profesor


#Obtener Cursos
@profesores_api.route("/api/v1/profesor", methods=['GET'])
def list():
    data = []
    for row in Profesor.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response


@profesores_api.route("/api/v1/profesor", methods=["POST"])
def create():
    primer_nombre = request.json['primer_nombre']
    segundo_nombre = request.json['segundo_nombre']
    primer_apellido = request.json['primer_apellido']
    segundo_apellido = request.json['segundo_apellido']
    profesion = request.json['profesion']
    correo = request.json['correo']

    profesor = Profesor()
    profesor.primerNombre = primer_nombre
    profesor.segundoNombre = segundo_nombre
    profesor.primerApellido = primer_apellido
    profesor.segundoApellido = segundo_apellido
    profesor.profesion = profesion
    profesor.correo = correo
    db.session.add(profesor)
    db.session.commit()

    return jsonify({'msg': profesor.to_json(), 'status': 'creado correctamente'})


@profesores_api.route("/api/v1/profesor/<id>", methods=["GET"])
def edit(id):
    profesor = Profesor.query.filter_by(id=id).first()
    if profesor is not None:
        response = jsonify({'profesor': profesor.to_json()})
    else:
        response = jsonify({'mensaje': 'Profesor no existe'})

    return response


@profesores_api.route("/api/v1/profesor/<id>", methods=["PUT"])
def update(id):
    profesor = Profesor.query.filter_by(id=id).first()
    if profesor is not None:
        # Obtenemos los datos que se van a actualizar

        primer_nombre = request.json['primer_nombre']
        segundo_nombre = request.json['segundo_nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        profesion = request.json['profesion']
        correo = request.json['correo']

        # Actualizamos los datos

        profesor.primerNombre = primer_nombre
        profesor.segundoNombre = segundo_nombre
        profesor.primerApellido = primer_apellido
        profesor.segundoApellido = segundo_apellido
        profesor.profesion = profesion
        profesor.correo = correo
        db.session.commit()

        response = jsonify({'profesor': profesor.to_json()})
    else:
        response = jsonify({'mensaje': 'Profesor no existe'})

    return response


@profesores_api.route("/api/v1/profesor/<id>", methods=["DELETE"])
def delete(id):
    profesor = Profesor.query.filter_by(id=id).first()
    if profesor is not None:
        db.session.delete(profesor)
        db.session.commit()
        return jsonify({'msg': 'Profesor con el ID ' + id + ' fue eliminado', 'registro': profesor.to_json()})
    else:
        return jsonify({'msg': 'Registro no encontrado'})
