from flask import Flask
from flask_restful import Api
from dev_by_id import Dev_by_id
from create_and_list_dev import Create_and_list_dev
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

api.add_resource(Dev_by_id, "/dev/<int:id>/")
api.add_resource(Create_and_list_dev, "/dev/")
api.add_resource(Habilidades, "/habilidades/")

if __name__ == "__main__":
    app.run(debug=True)