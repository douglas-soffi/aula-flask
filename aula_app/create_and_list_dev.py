from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json
from devs import devs

class Create_and_list_dev(Resource):
    
    def get(self):

        response = jsonify(devs) 
        return response

    def post(self):

        dados = json.loads(request.data)
        devs.append(dados)
        response = {
            "status":"Êxito",
            "mensagem":"Registro inserido"
        }
        return response