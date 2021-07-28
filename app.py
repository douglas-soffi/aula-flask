from flask import Flask, request, jsonify
import json

app = Flask(__name__)

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

@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def devs_by_id(id):

    if request.method == "GET":

        try:
            dev = devs[id]
            return dev

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Desenvolvedor {id} não existe"
            }
            return response

        except Exception:
            response = {
                "status":"Erro",
                "mensagem":"Erro desconhecido. Procure o administrador"
            }
            return response
        

    elif request.method == "PUT":

        try:
            dados = json.loads(request.data)
            devs[id] = dados
            return dados

        except Exception:
            response = {
                "status":"Erro",
                "mensagem":"Erro desconhecido. Procure o administrador"
            }
            return response

    elif request.method == "DELETE":

        try:
            devs.pop(id)
            return {
                "status":"Êxito",
                "mensagem":"Registro excluído"
            }

        except IndexError:
            response = {
                "status":"Erro",
                "mensagem":f"Desenvolvedor {id} não existe"
            }
            return response

        except Exception:
            response = {
                "status":"Erro",
                "mensagem":"Erro desconhecido. Procure o administrador"
            }
            return response

@app.route("/dev/", methods=["POST", "GET"])
def create_devs():

    if request.method == "POST":
        dados = json.loads(request.data)
        devs.append(dados)
        return {
            "status":"Êxito",
            "mensagem":"Registro inserido"
        }

    elif request.method == "GET":
        return jsonify(devs)

if __name__ == "__main__":
    app.run(debug=True)