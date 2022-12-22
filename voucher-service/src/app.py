import uuid
from flask import Flask, request
import db

from enum import Enum

app = Flask(__name__)

@app.get("/vouchers/<voucher_id>")
def get_voucher(voucher_id):
    voucher = db.get_voucher(voucher_id) 
    return voucher, 200

@app.get("/vouchers")
def get_vouchers():
    if "person_id" not in request.args:
        return 404

    person_id = request.args["person_id"]
    vouchers = db.get_vouchers(person_id) 
    return vouchers, 200

@app.post("/vouchers")
def create_voucher():
    voucher_id = str(uuid.uuid4())
    request_json = request.get_json()

    if "credits" not in request_json: 
        return 400

    credits = request_json["credits"]
    db.create_voucher(voucher_id, credits) 
    return {"voucher_id": voucher_id}, 201


@app.patch("/vouchers/<voucher_id>")
def update_voucher(voucher_id):
    request_json = request.get_json()

    if "type" not in request_json:
        return {"error": "Missing required field: type"}, 400

    type = request_json["type"]
    credits = request_json.get("credits", None)
    person_id = request_json.get("person_id", None)

    if type == "UPDATE_CREDITS":
        if not credits:
            return {"error": "Missing required field: credits"}, 400
        else:
            db.update_credits(voucher_id, credits)
            return '', 200

    elif type == "REDEEM_VOUCHER":
        if not person_id:
            return {"error": "Missing required field: person_id"}, 400
        else:
            db.redeem_voucher(voucher_id, person_id)
            return '', 200

    else:
        return {"error": "Unknown type. Valid options are REDEEM_VOUCHER or UPDATE_CREDITS."}, 422


