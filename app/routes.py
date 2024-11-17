from flask import request, jsonify
from app import app
from config.settings import guest_schedule

@app.route('/add_guest', methods=['POST'])
def add_guest():
    data = request.json
    plate = data['plate']
    start = data['start']
    end = data['end']
    guest_schedule[plate] = {"start": start, "end": end}
    return jsonify({"status": "Guest added successfully"}), 200

@app.route('/view_guests', methods=['GET'])
def view_guests():
    return jsonify(guest_schedule), 200
