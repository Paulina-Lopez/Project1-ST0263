from flask import Blueprint, jsonify, make_response, request
from src.services.auth import client_login, client_signup
from src.services.node import node_alive, create_node
from src.services.files import add_file, search_files


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    response = {
        "status": True,
        "message": "Namenode online"
    }
    return make_response(jsonify(response), 200)


# Client Endpoints
@routes.route('/login', methods=['POST'])
def login():
    request_body = request.json
    response = client_login(request_body.get('username'), request_body.get('password'))
    return make_response(response, 200)


# Node Endpoints
@routes.route('/node-on', methods=['POST'])
def node_on ():
    print('Node on')

    request_body = request.json
    return node_alive(request_body.get('ip'), request_body.get('port'))

@routes.route('/node-create', methods=['POST'])
def node_create ():
    request_body = request.json
    return create_node(request_body.get('name'), request_body.get('ip'), request_body.get('port'))


# Node files

@routes.route('/add-files', methods=['POST'])
def node_add_file ():
    request_body = request.json
    response = add_file(request_body)
    return make_response(jsonify(response), 200)

@routes.route('/search_files', methods=['POST'])
def search_file_name():
    request_body = request.json
    files = search_files(request_body["file_name"]) 
    return make_response(jsonify({"files": files}), 200)