from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from devs import devs

class Dev_by_id(Resource):

    def get(self, id):

        try:
            response = devs[id]

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Desenvolvedor {id} não existe"
            }
        return response
    
    def put(self, id):

        try:
            response = json.loads(request.data)
            devs[id] = response

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Desenvolvedor {id} não existe"
            }
        return response

    def delete(self, id):

        try:
            devs.pop(id)
            response = {
                "status":"Êxito",
                "mensagem":"Registro excluído"
            }

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Desenvolvedor {id} não existe"
            }
        return response