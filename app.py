from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

devs = [
    {
        "nome":"Douglas",
        "habilidades":[
            "Python",
            "Flask"
        ]
    },
    {
        "nome":"Soffi",
        "habilidades":[
            "Python",
            "Django"
        ]
    }
]

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

api.add_resource(Dev_by_id, "/dev/<int:id>/")
api.add_resource(Create_and_list_dev, "/dev/")

if __name__ == "__main__":
    app.run(debug=True)