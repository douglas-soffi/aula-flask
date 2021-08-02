from flask import jsonify
from flask_restful import Resource
import json

habilidades = [
    "Python",
    "Flask",
    "Django",
    "PHP",
    "Java",
    "C#",
    "C+",
    "C++"
]

class Habilidades(Resource):

    def get(self):
        response = jsonify(habilidades)
        return response