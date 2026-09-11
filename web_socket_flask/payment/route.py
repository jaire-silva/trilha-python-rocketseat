from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, send_file, render_template

from web_socket_flask.config import IMG_FOLDER, is_valid_qr_code_file
from web_socket_flask.database import db
from web_socket_flask.payment import Payment
from web_socket_flask.payment.payment_type import Pix

bp_payment = Blueprint('payment', __name__, url_prefix='/payment')


@bp_payment.route('/pix', methods=['POST'])
def pix():
    data = request.get_json()

    if "value" not in data:
        return jsonify({'message': 'Invalid value'}), 400

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(value=data['value'], expiration_date=expiration_date)

    pix_obj = Pix()

    data_payment_pix = pix_obj.create_payment()
    new_payment.bank_payment_id = data_payment_pix['bank_payment_id']
    new_payment.qr_code = data_payment_pix['qr_code']

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
    return render_template('payment.html')


@bp_payment.route('/pix/qr-code/<file_name>', methods=['GET'])
def payment_pix_qr_code(file_name):
    img_path = f"{IMG_FOLDER}/{file_name}.png"

    if not is_valid_qr_code_file(img_path):
        return render_template('404.html')

    return send_file(img_path, mimetype="image/png")