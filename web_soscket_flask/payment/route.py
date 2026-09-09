from flask import Blueprint, jsonify

bp_payment = Blueprint('payment', __name__, url_prefix='/payment')


@bp_payment.route('/pix', methods=['POST'])
def pix():
    return jsonify({'message': 'The payment has been created'})


@bp_payment.route('/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({'message': 'The payment has been confirmed'})

@bp_payment.route('/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return jsonify({'message': f'The payment with id {payment_id} has been found'})