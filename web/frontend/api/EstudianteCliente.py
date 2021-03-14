from flask import jsonify, json
import requests


class EstudianteCliente:

    @staticmethod
    def get_estudiantes():
        response = requests.get(url='http://estudiantes-api:5000/api/v1/estudiantes')
        if response:
            profesores = response.json()
        else:
            profesores = []
        return profesores

    @staticmethod
    def post_estudiante_create(form):
        estudiante = False
        payload = {
            'nombre_estudiante': form.nombreEstudiante.data,
            'direccion': form.direccion.data,
            'telefono': form.telefono.data,
            'identificacion': form.identificacion.data,
            'sede': form.sede.data
        }
        headers = {'content-type': 'application/json'}
        dataJson = json.dumps(payload)
        url = 'http://estudiantes-api:5000/api/v1/estudiantes'
        response = requests.post(url, data=dataJson, headers=headers)
        if response:
            estudiante = response.json()
        return estudiante
