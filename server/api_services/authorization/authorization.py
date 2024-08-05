from flask import Blueprint, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy
import os

auth_bp = Blueprint('auth', __name__)

CONFIG = {'AMQP_URI': os.getenv('AMQP_URI')}

@auth_bp.route('/sign-up', methods=['POST'])
def sign_up():
    data = request.json
    try:
        with ClusterRpcProxy(CONFIG) as rpc:
            response = rpc.auth_service.sign_up(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/log-in', methods=['GET'])
def log_in():
    data=request.json
    try:
        with ClusterRpcProxy(CONFIG) as rpc:
            response = rpc.auth_service.log_in(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
