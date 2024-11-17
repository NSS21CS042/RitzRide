import cv2

def recognize_license_plate(image_path):
    plate_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in plates:
        license_plate = img[y:y+h, x:x+w]
        print("License plate detected")
        return "ABC123"  # Example detected plate number
    return None
