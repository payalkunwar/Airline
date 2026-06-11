from flask import Flask, request, jsonify

app = Flask(__name__)

payments = []

@app.route('/payment', methods=['POST'])
def make_payment():

    data = request.json

    payment = {
        "payment_id": len(payments)+1,
        "booking_id": data["booking_id"],
        "amount": data["amount"],
        "status": "SUCCESS"
    }

    payments.append(payment)

    return jsonify(payment)


@app.route('/payments', methods=['GET'])
def get_payments():
    return jsonify(payments)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001)