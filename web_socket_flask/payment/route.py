from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request

from web_socket_flask.database import db
from web_socket_flask.payment import Payment

bp_payment = Blueprint('payment', __name__, url_prefix='/payment')


@bp_payment.route('/pix', methods=['POST'])
def pix():
    data = request.get_json()

    if "value" not in data:
        return jsonify({'message': 'Invalid value'}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        'message': 'The payment has been created',
        "payment": new_payment.to_dict()
    })


@bp_payment.route('/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({'message': 'The payment has been confirmed'})


@bp_payment.route('/pix/<int:payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return jsonify({'message': f'The payment with id {payment_id} has been found'})