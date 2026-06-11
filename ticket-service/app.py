from flask import Flask, request, jsonify

app = Flask(__name__)

tickets = []

@app.route('/ticket', methods=['POST'])
def generate_ticket():

    data = request.json

    ticket = {
        "ticket_id": len(tickets)+1,
        "booking_id": data["booking_id"],
        "seat":"12A"
    }

    tickets.append(ticket)

    return jsonify(ticket)


@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002)