from flask import Flask, request
from flask_cors import CORS
from dbcontroller import Database
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})


@app.route('/data/equipment', methods=["GET", "POST"])
def equipment_endpoint():
    if request.method == 'GET':
        return Database.get_equipment_list()
    elif request.method == 'POST':
        data = json.loads(request.data)
        if data['method'] == 'ADD':
            Database.add_equipment(data)
        elif data['method'] == 'EDIT':
            Database.edit_equipment(data)
        elif data['method'] == 'DELETE':
            Database.delete_equipment(data)
    return "True"


@app.route('/data/mol', methods=["GET", "POST", "DELETE"])
def mol_endpoint():
    if request.method == 'GET':
        return Database.get_mol_list()
    elif request.method == 'POST':
        data = json.loads(request.data)
        if data['method'] == 'ADD':
            Database.add_mol(data)
        elif data['method'] == 'EDIT':
            Database.edit_mol(data)
        elif data['method'] == 'DELETE':
            Database.delete_mol(data)
    return "True"


if __name__ == '__main__':
    app.run()