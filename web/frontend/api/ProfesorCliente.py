from flask import jsonify, json
import requests


class ProfesorCliente:

    @staticmethod
    def get_profesores():
        response = requests.get(url='http://profesores-api:5000/api/v1/profesor')
        if response:
            profesores = response.json()
        else:
            profesores = []
        return profesores

    @staticmethod
    def post_profesor_create(form):
        profesor = False
        payload = {
            'primer_nombre': form.primerNombre.data,
            'segundo_nombre': form.segundoNombre.data,
            'primer_apellido': form.primerApellido.data,
            'segundo_apellido': form.segundoApellido.data,
            'profesion': form.profesion.data,
            'correo': form.correo.data
        }
        headers = {'content-type': 'application/json'}
        dataJson = json.dumps(payload)
        print(dataJson)
        url = 'http://profesores-api:5000/api/v1/profesor'
        response = requests.post(url, data=dataJson, headers=headers)
        print(response)
        if response:
            profesor = response.json()
        return profesor
