from flask import jsonify, json
import requests


class CursosCliente:

    @staticmethod
    def get_cursos():
        response = requests.get(url='http://cursos-api:5000/api/v1/curso')
        if response:
            cursos = response.json()
        else:
            cursos = []
        return cursos

    @staticmethod
    def post_curso_create(form):
        curso = False
        payload = {
            'nombre': form.nombreCurso.data,
            'descripcion': form.descripcion.data,
            'sede': form.horas.data,
            'horas': form.sede.data,
            'id_profesor': '1'
        }
        headers = {'content-type': 'application/json'}
        dataJson = json.dumps(payload)
        print(dataJson)
        url = 'http://cursos-api:5000/api/v1/curso'
        response = requests.post(url, data=dataJson, headers=headers)
        print(response)
        if response:
            curso = response.json()
        return curso
