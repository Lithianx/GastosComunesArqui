from flask import Blueprint, request, jsonify
from controllers.GastoComunController import GastoComunController

gastos_blueprint = Blueprint('gastos_blueprint', __name__)

@gastos_blueprint.route('/gastos/create', methods=['POST'])
def generar_pago():
    data = request.get_json()
    try:
        nuevo_pago = GastoComunController.generar_pago_controller(
            num_depto=data.get('num_depto'),
            monto=data.get('monto'),
            periodo=data.get('periodo'),
            fecha_pago=data.get('fecha_pago'),
            estado_pago=data.get('estado_pago', 'pendiente')
        )
        return jsonify({"mensaje": "Pago creado", "gasto_comun": nuevo_pago.serialize()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@gastos_blueprint.route('/gastos/<int:id_gasto_comun>/marcar_pago', methods=['PUT'])
def marcar_pago(id_gasto_comun):
    data = request.get_json()
    estado_pago = data.get('estado_pago')
    pago_actualizado = GastoComunController.marcar_pago_controller(id_gasto_comun, estado_pago)
    
    if pago_actualizado:
        return jsonify({"mensaje": "Pago actualizado", "gasto_comun": pago_actualizado.serialize()}), 200
    return jsonify({"mensaje": "Pago no encontrado"}), 404

@gastos_blueprint.route('/gastos/<int:id_gasto_comun>', methods=['GET'])
def obtener_pago(id_gasto_comun):
    pago = GastoComunController.obtener_pago_controller(id_gasto_comun)
    if pago:
        return jsonify(pago.serialize()), 200
    return jsonify({"mensaje": "Pago no encontrado"}), 404
