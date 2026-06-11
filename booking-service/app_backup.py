from flask import Flask, request, jsonify

app = Flask(__name__)

bookings = []

@app.route('/flights', methods=['GET'])
def flights():

    flight_data = [
        {
            "flight_id": "AI101",
            "source": "Mumbai",
            "destination": "Delhi"
        },
        {
            "flight_id": "AI102",
            "source": "Delhi",
            "destination": "Bangalore"
        }
    ]

    return jsonify(flight_data)


@app.route('/book', methods=['POST'])
def book_flight():

    data = request.json

    booking = {
        "booking_id": len(bookings)+1,
        "name": data["name"],
        "flight_id": data["flight_id"]
    }

    bookings.append(booking)

    return jsonify({
        "message":"Booking Successful",
        "booking":booking
    })


@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
    