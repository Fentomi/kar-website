from flask import Flask, request
from flask_cors import CORS
from dbcontroller import Database
import json

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})
CORS(app, resources={r"/*": {"origins": "http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})


@app.route('/data/client', methods=["GET", "POST"])
def client_endpoint():
    if request.method == 'GET':
        return Database.get_client_list()
    elif request.method == 'POST':
        data = json.loads(request.data)
        if data['method'] == 'ADD':
            return Database.add_client(data)
        elif data['method'] == 'EDIT':
            return Database.edit_client(data)
        elif data['method'] == 'DELETE':
            return Database.delete_client(data)

@app.route('/data/order', methods=["GET", "POST"])
def order_endpoint():
    if request.method == 'GET':
        return Database.get_order_list()
    elif request.method == 'POST':
        data = json.loads(request.data)
        if data['method'] == 'ADD':
            return Database.add_order(data)
        elif data['method'] == 'EDIT':
            return Database.edit_order(data)
        elif data['method'] == 'DELETE':
            return Database.delete_order(data)


@app.route('/data/employee', methods=["GET"])
def employee_endpoint():
    return Database.get_employee_list()


@app.route('/data/product', methods=["GET"])
def product_endpoint():
    return Database.get_product_list()


if __name__ == '__main__':
    app.run()