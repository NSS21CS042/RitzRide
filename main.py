from app.utils import get_gps_location, is_vehicle_near_gate, control_gate, control_lights, is_guest_allowed
from app.license_plate import recognize_license_plate
from config.settings import guest_schedule

def main_workflow():
    vehicle_loc = (12.971598, 77.594566)  # Example vehicle location
    gate_loc = (12.971600, 77.594570)    # Example gate location
    image_path = "static/license_plate.jpg"  # Path to the license plate image

    if is_vehicle_near_gate(vehicle_loc, gate_loc):
        plate_number = recognize_license_plate(image_path)
        
        if plate_number and is_guest_allowed(plate_number, guest_schedule):
            control_gate(True)
            control_lights("on")
        else:
            print("Vehicle not recognized or not allowed")
    else:
        print("Vehicle not near gate")

if __name__ == "__main__":
    main_workflow()
