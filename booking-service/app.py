from flask import Flask, request, jsonify

app = Flask(__name__)

from db import connection, cursor

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

    query = """
    INSERT INTO bookings
    (passenger_name, flight_id)
    VALUES (%s,%s)
    """

    values = (
        data["name"],
        data["flight_id"]
    )

    cursor.execute(query, values)

    connection.commit()

    return jsonify({
        "message": "Booking Successful"
    })

@app.route('/bookings', methods=['GET'])
def get_bookings():

    cursor.execute(
        "SELECT * FROM bookings"
    )

    result = cursor.fetchall()

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)