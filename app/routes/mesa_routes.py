from flask import Blueprint, request, jsonify
import requests
import json
from app.config import SUPABASE_URL, HEADERS

mesa_bp = Blueprint('mesa_bp', __name__)

# GET /api/mesa -> todas las mesas
@mesa_bp.route('', methods=['GET'])
def get_mesas():
    response = requests.get(SUPABASE_URL, headers=HEADERS)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    if response.ok:
        return jsonify(response.json())
    return jsonify({
        "error": "No se pudieron obtener las mesas",
        "status_code": response.status_code,
        "response": response.text
    }), 500

# GET /api/mesa/<id> -> mesa específica
@mesa_bp.route('/<int:id>', methods=['GET'])
def get_mesa(id):
    url = f"{SUPABASE_URL}?id=eq.{id}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    if data:
        return jsonify(data[0])
    return jsonify({"error": "Mesa no encontrada"}), 404

# POST /api/mesa -> crear mesa
@mesa_bp.route('', methods=['POST'])
def create_mesa():
    capacidad = request.json.get("capacidad")
    payload = json.dumps({"capacidad": capacidad})
    response = requests.post(SUPABASE_URL, headers=HEADERS, data=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    if response.ok:
        return jsonify({"message": "Mesa creada"}), 201
    return jsonify({
        "error": "No se pudo crear la mesa",
        "status_code": response.status_code,
        "response": response.text
    }), 500

# PUT /api/mesa/<id> -> actualizar mesa
@mesa_bp.route('/<int:id>', methods=['PUT'])
def update_mesa(id):
    capacidad = request.json.get("capacidad")
    payload = json.dumps({"capacidad": capacidad})
    url = f"{SUPABASE_URL}?id=eq.{id}"
    response = requests.patch(url, headers=HEADERS, data=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    if response.ok:
        return jsonify({"message": "Mesa actualizada"})
    return jsonify({
        "error": "No se pudo actualizar la mesa",
        "status_code": response.status_code,
        "response": response.text
    }), 500

# DELETE /api/mesa/<id> -> eliminar mesa
@mesa_bp.route('/<int:id>', methods=['DELETE'])
def delete_mesa(id):
    url = f"{SUPABASE_URL}?id=eq.{id}"
    response = requests.delete(url, headers=HEADERS)
    if response.ok:
        return jsonify({"message": "Mesa eliminada"})
    return jsonify({"error": "No se pudo eliminar la mesa"}), 500
