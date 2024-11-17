import time
import serial
from datetime import datetime

def get_gps_location():
    gps = serial.Serial('/dev/ttyAMA0', baudrate=9600, timeout=1)  # Update port as needed
    while True:
        data = gps.readline().decode('ascii', errors='replace')
        if data.startswith('$GPRMC'):  # Example GPS sentence
            fields = data.split(',')
            latitude = fields[3]
            longitude = fields[5]
            return latitude, longitude

def is_vehicle_near_gate(vehicle_location, gate_location, radius=0.01):
    lat_diff = abs(vehicle_location[0] - gate_location[0])
    long_diff = abs(vehicle_location[1] - gate_location[1])
    return lat_diff < radius and long_diff < radius

def control_gate(open_gate):
    if open_gate:
        print("Gate Opening...")
        # GPIO control to open the gate
    else:
        print("Gate Closing...")
        # GPIO control to close the gate

def control_lights(state):
    if state == "on":
        print("Turning lights ON")
        # API call to turn on lights
    elif state == "off":
        print("Turning lights OFF")
        # API call to turn off lights

def is_guest_allowed(plate_number, guest_schedule):
    now = datetime.now().strftime("%H:%M")
    if plate_number in guest_schedule:
        start_time = guest_schedule[plate_number]["start"]
        end_time = guest_schedule[plate_number]["end"]
        return start_time <= now <= end_time
    return False
