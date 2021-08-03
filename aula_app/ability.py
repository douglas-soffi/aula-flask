from flask import jsonify, request
from flask_restful import Resource
import json

ability = [
    "Python",
    "Flask",
    "Django",
    "PHP",
    "Java",
    "C#",
    "C+",
    "C++"
]

class Ability_by_id(Resource):

    def get(self, id):
        
        try:
            response = ability[id]

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Habilidade {id} não existe"
            }
        return response

    def put(self, id):

        try:
            response = json.loads(request.data)
            ability[id] = response

        except IndexError:
                response = {
                "status":"Erro",
                "mensagem":f"Habilidade {id} não existe"
            }
        return response

    def delete(self, id):

        try:
            ability.pop(id)
            response = {
                "status":"Êxito",
                "menssagem":"Rgistro excluído"
            }

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Habilidade {id} não existe"
            }
            return response

class Create_and_list_ability(Resource):

    def get(self):

        response = jsonify(ability)
        return response

    def post(self):

        dados = json.loads(request.data)
        ability.append(dados)
        response = {
            "status":"Êxito",
            "mensagem":"Habilidade inserida"
        }
        return response