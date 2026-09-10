import os
import uuid

import qrcode

from web_socket_flask.config import IMG_FOLDER


class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        bank_payment_id = uuid.uuid4()
        hash_payment = f"has_payment_{bank_payment_id}"
        qrcode_img = qrcode.make(hash_payment)

        img_path = os.path.join(IMG_FOLDER, f"{bank_payment_id}.png")
        qrcode_img.save(img_path)

        return {
            "bank_payment_id": bank_payment_id,
            "qr_code": f"qr_code_payment_{bank_payment_id}",
        }