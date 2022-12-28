import uuid
import db

from flask import Flask, request, make_response
from waitress import serve

app = Flask(__name__)

@app.get("/vouchers/<voucher_id>")
def get_voucher(voucher_id):
    voucher = db.get_voucher(voucher_id) 

    if not voucher:
        return 404
    else:
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

    if "request_type" not in request_json:
        return {"error": "Missing required field: request_type"}, 400

    request_type = request_json["request_type"]
    credits = request_json.get("credits", None)
    person_id = request_json.get("person_id", None)

    if request_type == "ADD_CREDITS":
        if not credits:
            return {"error": "Missing required field: credits"}, 400
        else:
            db.add_credits(voucher_id, credits)
            return '', 200

    elif request_type == "SUBTRACT_CREDITS":
        if not credits:
            return {"error": "Missing required field: credits"}, 400
        else:
            db.subtract_credits(voucher_id, credits)
            return '', 200

    elif request_type == "REDEEM_VOUCHER":
        if not person_id:
            return {"error": "Missing required field: person_id"}, 400
        else:
            db.redeem_voucher(voucher_id, person_id)
            return '', 200

    else:
        return {"error": "Unknown request type. Valid options are REDEEM_VOUCHER or SUBTRACT_CREDITS."}, 422


if __name__ == '__main__':
    db.init()
    serve(app, host='0.0.0.0', port=8080)

