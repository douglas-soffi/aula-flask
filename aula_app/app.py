from flask import Flask
from flask_restful import Api
from dev import Dev_by_id, Create_and_list_dev
from ability import Ability_by_id, Create_and_list_ability

app = Flask(__name__)
api = Api(app)

api.add_resource(Dev_by_id, "/dev/<int:id>/")
api.add_resource(Create_and_list_dev, "/dev/")
api.add_resource(Ability_by_id, "/habilidade/<int:id>/")
api.add_resource(Create_and_list_ability, "/habilidade/")

if __name__ == "__main__":
    app.run(debug=True)